import os, sys
from setuptools import setup, find_packages

def read_requirements():
    """Parse requirements from requirements.txt."""
    reqs_path = os.path.join('.', 'requirements.txt')
    with open(reqs_path, 'r') as f:
        requirements = [line.rstrip() for line in f]
    return requirements

try:
    with open('README.md') as f:
        readme = f.read()
except IOError:
    readme = ''

try:
    with open('LICENSE') as f:
        license = f.read()
except IOError:
    license = ''

setup(
    name='actuapy',
    version='0.0.1',
    description='useful snippets for actuaries',
    long_description=readme,
    author='Rei Mizuta',
    author_email='ayanamizuta832@gmail.com',
    install_requires=read_requirements(),
    url='https://github.com/ayanamizuta/actuary',
    license=license,
    packages=find_packages(exclude=('tests', 'docs')),
    test_suite='tests'
)
