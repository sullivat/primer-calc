# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='primer-calc',
    version='0.0.1',
    description='A simple primer calculator',
    long_description=readme,
    author='Timothy Sullivan',
    author_email='sullivan.timm@gmail.com',
    url='https://github.com/sullivat/primer-calc',
    license=license,
    packages=find_packages(exclude=('tests'))
)
