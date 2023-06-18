pragma solidity ^0.8.0;

import {PrecompilesAPI} from "../../node_modules/@zondax/filecoin-solidity/contracts/v0.8/PrecompilesAPI.sol";
import '../../node_modules/@zondax/filecoin-solidity/contracts/v0.8/types/CommonTypes.sol';

contract direct_precompile_test {
    address constant RESOLVE_ADDRESS_PRECOMPILE_ADDR = 0xFE00000000000000000000000000000000000001;
    address constant LOOKUP_DELEGATED_ADDRESS_PRECOMPILE_ADDR = 0xfE00000000000000000000000000000000000002;
    bool isLocked = true;
    bool isProtected = true;

    modifier onlyOwner() {
        require(isProtected);
        _;
    }

    function initialize(bool _isLocked) external {
        /* Does some contract setup */
        isLocked = _isLocked;
    }

    function directPrecompile_1(bytes memory _data) external {
        require(!isLocked);
        (bool success, bytes memory raw_response) = 0xFE00000000000000000000000000000000000001.staticcall(_data);
        /* Does some normal logic */
    }

    function directPrecompile_2(bytes memory _data) external {
        require(!isLocked);
        (bool success, bytes memory raw_response) = 0xfE00000000000000000000000000000000000002.staticcall(_data);
        /* Does some normal logic */
    }

    function notSoDirectPrecompile_1(bytes memory _data) external {
        require(!isLocked);
        (bool success, bytes memory raw_response) = RESOLVE_ADDRESS_PRECOMPILE_ADDR.staticcall(_data);
    }

    function notSoDirectPrecompile_2(bytes memory _data) external {
        require(!isLocked);
        (bool success, bytes memory raw_response) = LOOKUP_DELEGATED_ADDRESS_PRECOMPILE_ADDR.staticcall(_data);
    }

}

contract direct_precompile_ok {
    bool isLocked = true;
    bool isProtected = true;

    modifier onlyOwner() {
        require(isProtected);
        _;
    }

    function initialize(bool _isLocked) onlyOwner external {
        /* Does some contract setup */
        isLocked = _isLocked;
    }

    function callPrecompile_1(CommonTypes.FilAddress memory _addr) external {
        require(!isLocked);
        PrecompilesAPI.resolveAddress(_addr);
        /* Does some normal logic */
    }

    function callPrecompile_2(uint64 _actor_id) external {
        require(!isLocked);
        PrecompilesAPI.lookupDelegatedAddress(_actor_id);
        /* Does some normal logic */
    }
}