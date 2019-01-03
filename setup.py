#!/usr/bin/env python3

from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(name='radicale-auth-sasl',
      version='0.1.0',
      description='radicale plugin for sasl authentication',
      long_description=long_description,
      author='Paul Fariello',
      author_email='paul@fariello.eu',
      url='https://github.com/paulfariello/radicale-auth-sasl',
      packages=find_packages())
