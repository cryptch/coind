from setuptools import setup, find_packages

setup(
    name='coind',
    version='1.0.0',
    description='A bitcoind based wallet manager in Python',
    long_description='This is a cryptocurrency wallets management using Python, ' +
                     'compatible with all bitcoind forked daemon.\n'+
                     'It will turn possible to execute commands like "-daemon" to "walletpassphrase"',
    license='MIT',
    author='Cryptch',
    author_email='fukuroh1@gmail.com',
    keywords=['coind', 'bitcoin', 'bitcoind', 'crypto', 'cryptch'],
    url='https://github.com/cryptch/coind',
    packages=find_packages(exclude=('coind.egg-info', 'dist', 'docker', 'test', 'venv')),
)
