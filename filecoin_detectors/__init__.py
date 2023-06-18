from filecoin_detectors.detectors.direct_precompile import DirectPrecompile


def make_plugin():
    plugin_detectors = [
        DirectPrecompile,
    ]
    plugin_printers = []

    return plugin_detectors, plugin_printers