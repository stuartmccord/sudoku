# -*- coding: utf-8 -*-

# Learn more: https://github.com/kennethreitz/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='sudoku',
    version='0.1.0',
    description='Package to solve sudoku',
    author='Stuart McCord',
    author_email='stuart.mccord@gmail.com',
    url='https://github.com/kennethreitz/samplemod',
    packages=find_packages()
)
