from setuptools import setup

with open('README.rst', encoding="utf-8") as f:
    readme = f.read()

setup(
        name='cryptocompare_api',
        version='0.1',
        description='Wrapper for CryptoCompare HTTP API',
        long_description=readme,
        url='https://github.com/W-McDonald/cryptocompare_api',
        author='W-McDonald',
        keywords='crypto cryptocurrency wrapper cryptocompare bitcoin ethereum trading exchange',
        license='MIT',
        python_requires='>=3',
        packages=['cryptocompare_api'],
        classifiers=['Programming Language :: Python :: 3'],
        install_requires=['requests']
        )

