# Direct Precomiple Usage

## Configuration
* Check: `fc-direct-precompile`
* Severity: `Medium`
* Confidence: `High`

## Description
The detector sees if a contract contains a direct usage of filecoin [precompiles](https://medium.com/@rbkhmrcr/precompiles-solidity-e5d29bd428c4).
Direct precompile usage might be dangerous due to missing checks that may to lead to DoS ([Denial of Service](https://medium.com/@Knownsec_Blockchain_Lab/in-depth-understanding-of-denial-of-service-vulnerabilities-dd437b1d7a1c)) or unexpected smart contract behaviour.


## Vulnerable Scenario
[test scenarios](../tests/direct_precompile_test.sol)

## Recommendation
Use Filecoin precompiles through filecoin-solidity library - https://github.com/Zondax/filecoin-solidity/blob/master/contracts/v0.8/PrecompilesAPI.sol
