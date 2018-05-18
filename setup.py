from setuptools import setup, find_packages

setup(
    name='coind',
    version='1.0.0',
    description='A bitcoind based wallet manager in Python',
    license='MIT',
    author='Cryptch',
    author_email='fukuroh1@gmail.com',
    keywords=['coind', 'bitcoin', 'bitcoind', 'crypto', 'cryptch'],
    url='https://gitlab.com/cryptch/coind',
    packages=find_packages(exclude=('coind.egg-info', 'dist', 'docker', 'tests', 'venv')),
)
