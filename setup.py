#!/usr/bin/env python
from setuptools import setup


setup(
    name="beetsdl-dev",
    version="0.0.1",
    description="Simple CLI wrapper integrating youtube-dl and beets.",
    author="Alex Khoma",
    url="https://github.com/alexkhoma99/beetsdl",
    install_requires=[
        "beets",
        "colorama",
    ],
    packages=["beetsdl"],
    keywords=["youtube-dl", "beets", ],
    classifiers=[],
    entry_points={
        "console_scripts": ["beetsdl=beetsdl.cli:main"]
    },
)
