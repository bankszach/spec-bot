"""Setup file for SoloChain package."""

from setuptools import setup, find_packages

setup(
    name="solochain",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "langchain>=0.1.0",
        "langchain-openai>=0.0.5",
        "langchain-community>=0.0.5",
        "openai>=1.0.0",
        "python-dotenv>=1.0.0",
    ],
) 