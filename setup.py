#!/usr/bin/env python
__usage__ = "setup.py command [--options]"
__description__ = "standard install script"
__author__ = "Reed Essick (reed.essick@ligo.org)"
# Modified by Pinchen Fan (pinchen.fan@ligo.org)
#-------------------------------------------------

from setuptools import (setup, find_packages)
import glob

setup(
    name = 'skymap_statistics',
    version = '0.0',
    url = 'https://gitlab.com/pinchen.fan/skymap_statistics',
    author = __author__,
    author_email = 'pinchen.fan@ligo.org',
    description = __description__,
    license = 'MIT',
    scripts = glob.glob('bin/*'),
    packages = find_packages(),
    data_files = [],
    package_data = {
        'skymap_statistics.PSDs': ['*.txt'],
        'skymap_statistics.plotting': ['*.json'],
    },
    requires = [],
)
