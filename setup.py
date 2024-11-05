#!/usr/bin/env python
# coding: utf-8

# Copyright (c) Jupyter Development Team.
# Distributed under the terms of the Modified BSD License.

#-----------------------------------------------------------------------------
# Minimal Python version sanity check (from IPython/Jupyterhub)
#-----------------------------------------------------------------------------

from __future__ import print_function

import os
import sys

#from distutils.core import setup
from setuptools import setup, find_packages

pjoin = os.path.join
here = os.path.abspath(os.path.dirname(__file__))

# Get the current package version.
version_ns = {}
with open(pjoin(here, 'version.py')) as f:
    exec(f.read(), {}, version_ns)

# Read the requirements from the requirements.txt file
install_requires = []
if os.path.exists('requirements.txt'):
    with open('requirements.txt') as f:
        install_requires = [
            line.strip()
            for line in f.readlines()
            if line.strip() and not line.startswith(('#', '-e'))
        ]
        
setup_args = dict(
    name                = 'wrapspawner',
    #packages            = ['wrapspawner'],
    version             = version_ns['__version__'],
    description         = """Wrapspawner: A spawner for Jupyterhub to wrap other spawners and allow the user to choose among them.""",
    long_description    = "",
    author              = "Michael Milligan",
    author_email        = "milligan@umn.edu",
    url                 = "http://jupyter.org",
    license             = "BSD",
    platforms           = "Linux, Mac OS X",
    keywords            = ['Interactive', 'Interpreter', 'Shell', 'Web'],
    classifiers         = [
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
    ],
    packages=find_packages(),  # Automatically finds all packages under the current directory
    install_requires=install_requires,  # List of dependencies
    include_package_data=True,  # Include files as specified in MANIFEST.in
)

def main():
    setup(**setup_args)

if __name__ == '__main__':
    main()
