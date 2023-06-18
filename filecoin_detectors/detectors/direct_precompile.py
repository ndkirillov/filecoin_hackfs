from typing import List
from slither.utils.output import Output
from slither.detectors.abstract_detector import AbstractDetector, DetectorClassification
from slither.core.declarations import Function
#from slither.slithir.operations import LibraryCall


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


    def _has_direct_precompile (self, fun: Function) -> bool:   #если есть low level static call и используется в правой части адрес прекомпайла - это вхождение
        """Checks if a function calls precompile directly"""
        if isinstance(fun, Function):   # check for a correct function type
                if fun.low_level_calls:
                    if 'staticcall' in str(fun.low_level_calls[0]):
                        for node in fun.nodes:
                            if '0xFE00000000000000000000000000000000000001' in str(node) or '0xfE00000000000000000000000000000000000002' in str(node):
                                return True
        return False


    def _detect(self) -> List[Output]:
        """Main function"""
        res = []
        for contract in self.compilation_unit.contracts_derived:
            for f in contract.functions_and_modifiers_declared:
                x = self._has_direct_precompile(f)
                if x:
                    res.append(self.generate_result([
                        "Direct precompile call in ",
                        f,
                        '\n']))
        return res
