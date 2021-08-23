#!/usr/bin/env python3
""" A collection of potentially useful designed tools for use in Notebooks.

It provides:

- A lightweight image viewer

"""

from setuptools import setup, find_packages

requirements = [
    "numpy",
    "matplotlib",
    "ipympl",
    "Pillow",
]


setup(
    name="Notebook Gizmos",
    url="https://github.com/matthewpurri/notebook-gizmos",
    author="Matt Purri",
    author_email="mpurri.dev@gmail.com",
    packages=find_packages(exclude=["tests"]),
    install_requires=requirements,
    version="0.1.0",
    license="CC0 1.0 Universal",
    description="A collection of potentially useful designed tools for use in Notebooks (Jupyter-Notebook, JupyterLab).",
)
