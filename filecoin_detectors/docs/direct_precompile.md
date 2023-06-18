# Direct Precomiple Usage

## Configuration
* Check: `fc-direct-precompile`
* Severity: `Medium`
* Confidence: `High`

## Description
The detector sees if a contract contains a direct usage of filecoin precompiles.


## Vulnerable Scenario
[test scenarios](../tests/direct_precompile_test.sol)

## Recommendation
Use Filecoin precompiles through filecoin-solidity library - https://github.com/Zondax/filecoin-solidity/blob/master/contracts/v0.8/PrecompilesAPI.sol
