from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'simplerApps Python Analyze package'
LONG_DESCRIPTION = 'Data Science - Scores Analysis functions'

setup(
    name='sapy_analyze',
    version=VERSION,
    description=DESCRIPTION,
    long_description=LONG_DESCRIPTION,
    install_requires=[
        'pandas>=2.1.0',  # Specify the minimum version of Pandas required
    ],
    packages=find_packages(),
)