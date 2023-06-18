from setuptools import setup, find_packages

setup(
    name="slither-filecoin",
    description="This is a plugin of filecoin detectors",
    url="https://github.com/ndkirillov/filecoin_hackfs",
    author="ndkirillov and eMarchenko",
    version="0.1",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=["slither-analyzer==0.1"],
    entry_points={
        "slither_analyzer.plugin": "slither my-plugin=slither_my_plugin:make_plugin",
    },
)