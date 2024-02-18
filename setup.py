from setuptools import setup, find_packages

setup(
    name="unpyc37",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        # List any dependencies here
    ],
    entry_points={
        'console_scripts': [
            'unpyc37 = unpyc37.unpyc3:main_function',
        ],
    },
    description="Decompiler for Python 3.7 (forked from https://github.com/andrews4s/unpyc37)",
    url="https://github.com/bubicle/unpyc37",
)