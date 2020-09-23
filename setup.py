"""
Setup for lookatme.contrib.image_ueberzug
"""


from setuptools import setup, find_namespace_packages
import os


setup(
    name="lookatme.contrib.image_ueberzug",
    version="0.0.0",
    description="An image renderer that uses ueberzug",
    author="",
    author_email="",
    python_requires=">=3.5",
    packages=find_namespace_packages(include=["lookatme.*"]),
)
