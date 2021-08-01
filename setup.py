"""The python wrapper for Binary API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="binaryapi",
    version="0.2.5",
    packages=find_packages(),
    install_requires=["requests", "websocket-client", "simplejson", "pause", "rich"],
    include_package_data=True,
    description="Binary.com API for Python",
    long_description="Binary.com API for Python",
    url="https://github.com/mdn522/binaryapi",
    author="Abdullah Mallik",
    author_email="mdn522@gmail.com",
    zip_safe=False
)
