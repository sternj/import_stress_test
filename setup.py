from setuptools import setup, find_packages

setup(
    name="import_stress_test",
    version="0.1",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "import_stress_test = import_stress_test.main:main_function",
        ],
    },
)