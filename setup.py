from setuptools import setup, find_packages
from pathlib import Path
import codecs
import os

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

VERSION = '0.0.1'
DESCRIPTION = 'Package for the toxauth.me API'

setup(
    name="ToxAuth",
    version=VERSION,
    author="Toxary",
    author_email="<mail@toxary.me>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['requests', 'pycryptodome', 'fingerprint'],
    keywords=['wrapper', 'apiwrapper', 'toxauth', 'auth', 'authsystem', 'toxauth.me'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)
