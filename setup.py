#!/usr/bin/env python3
from setuptools import setup, find_packages

setup(
    name="FunctionalTools",
    version="0.0.1",
    author="Jose hdz",
    author_email="jhernandez.sld@gmail.com",
    description=("Tools for fp"),
    py_modules=["src"],
    license="MIT",
    keywords="python functional programming",
    url="http://github.com/ppgodel/FunctionalTools",
    packages=find_packages(),
)
