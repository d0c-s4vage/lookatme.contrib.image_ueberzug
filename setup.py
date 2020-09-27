"""
Setup for lookatme.contrib.image_ueberzug
"""


from setuptools import setup, find_namespace_packages
import os


req_path = os.path.join(os.path.dirname(__file__), "requirements.txt")
with open(req_path, "r") as f:
    required = f.read().splitlines()


setup(
    name="lookatme.contrib.image_ueberzug",
    version="0.0.0",
    description="An image renderer that uses ueberzug",
    author="",
    author_email="",
    python_requires=">=3.5",
    packages=find_namespace_packages(include=["lookatme.*"]),
    #install_requires=required,
)
