import os, sys
from setuptools import setup, find_packages

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

setup(
    name='actuary',
    version='0.0.1',
    description='useful snippets for actuaries',
    long_description="README.md",
    author='Rei Mizuta',
    author_email='ayanamizuta832@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/ayanamizuta/actuary',
    license="LICENSE",
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
