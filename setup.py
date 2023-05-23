#! /usr/bin/env python3
"""
Setup for casavlbitools
"""
import os
import sys
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...


def read(fname):
    """Read a file"""
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


def get_version():
    """Get the version number of casavlbitools"""
    import casavlbitools as cvt
    return cvt.__version__


reqs = ['astropy']


setup(
    name="casavlbitools",
    version=get_version(),
    author="jive-vlbi",
    description="Scripts to assist VLBI data reduction in CASA.",
    url="https://github.com/jive-vlbi/casa-vlbi",
    long_description=read('README.md'),
    long_description_content_type='text/markdown',
    packages=['casavlbitools'],
    install_requires=reqs,
    scripts=['append_gc.py',   
             'append_wx.py',   
             'fix_idi.py',
             'gc.py',
             'importtsys.py',
             'append_tsys.py', 
             'eop.py',
             'flag.py',
             'gc2.py',
             'model.py']
)