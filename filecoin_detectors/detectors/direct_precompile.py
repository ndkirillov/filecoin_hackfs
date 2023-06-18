from typing import List
from slither.utils.output import Output
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.core.declarations import Function


class DirectPrecompile(AbstractDetector):
    """
    Sees if a contract has a direct precompile usage.
    """

    ARGUMENT = 'fc-direct-precompile' # slither will launch the detector with slither.py --detect mydetector
    HELP = 'precompiles are called directly, not through a library'
    IMPACT = DetectorClassification.MEDIUM
    CONFIDENCE = DetectorClassification.HIGH

    WIKI = 'https://github.com/Zondax/filecoin-solidity/blob/master/contracts/v0.8/PrecompilesAPI.sol'
    WIKI_TITLE = 'Direct Precompile Usage'
    WIKI_DESCRIPTION = "-"
    WIKI_EXPLOIT_SCENARIO = '-'
    WIKI_RECOMMENDATION = 'Use precompiles through filecoin library'


    def _has_direct_precompile (self, fun: Function) -> bool: # function checks if there are direct precompile calls in the code
        precompile_address_1 = '0xFE00000000000000000000000000000000000001'
        precompile_address_2 = '0xfE00000000000000000000000000000000000002'
        if isinstance(fun, Function):   # check for a correct function type
            for node in fun.nodes:
                if 'staticcall' in str(node): # precompiles are called with staticcalls
                    if precompile_address_1 in str(node) or precompile_address_2 in str(node):
                        return True
                    for var in node.variables_read:
                        if precompile_address_1 in str(var.expression) or precompile_address_2 in str(var.expression):
                            return True


    def _detect(self) -> List[Output]:
        """Main function"""
        res = []
        for contract in self.compilation_unit.contracts_derived:
            if 'PrecompilesAPI' not in contract.name:
                for f in contract.functions_and_modifiers_declared:
                    x = self._has_direct_precompile(f)
                    if x:
                        res.append(self.generate_result([
                            "Direct precompile call in ",
                            f,
                            '\n']))
        return res
