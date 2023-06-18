# filecoin_hackfs
A static analysis plugin with filecoin integration vulnerability detectors. Plugin uses [Slither](https://github.com/crytic/slither/) engine.
For the demo [Filecoin-solidity](https://github.com/Zondax/filecoin-solidity/) was audited.

## Repo structure
* [Docs](./filecoin_detectors/docs/) - vulnerability and detector descriptions, recommendations on fixes.
* [Detectors](./filecoin_detectors/detectors/) - detectors code.
* [Tests](./filecoin_detectors/tests/) - smart contracts with cases where detector should and should not work.

## How to install
1. Install original Slither [Slither](https://github.com/crytic/slither/).
2. In the current repo run `npm install` and `sudo python3 setup.py develop` (on Linux).

## How to use
After the installation detectors are included into original Slither. Run Slither as usual.
To run demo detector type in terminal `slither ./pathToFile --detect "fc-direct-precompile"`