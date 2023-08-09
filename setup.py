from setuptools import setup, find_packages

setup(
    name="mymodule",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "mymodule = mymodule.main:main_function",
        ],
    },
)