from setuptools import setup


with open("README.md","r", encoding="utf-8")as fh :
    long_description=fh.read()

AUTHOR_NAME= 'SRIRAM'
SRC_REPO= 'src'
LIST_OF_REQUIREMENTS = ['stremlit']

setup(
    name=SRC_REPO,
    version= '0.0.1',
    author=AUTHOR_NAME,
    description='A small example package for movie recommendation',
    long_description=long_description,
    package = [SRC_REPO],
    python_requires = '>=3.13',
    install_requires = LIST_OF_REQUIREMENTS,
)
