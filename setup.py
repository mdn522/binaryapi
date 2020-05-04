"""The python wrapper for Binary API package setup."""
from setuptools import (setup, find_packages)

setup(
    name="binaryapi",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["requests", "websocket-client==0.56"],
    include_package_data=True,
    description="Binary.com API for python",
    long_description="Binary.com API for python",
    url="https://github.com/mdn522/binaryapi",
    author="Abdullah Mallik",
    author_email="mdn522@gmail.com",
    zip_safe=False
)
