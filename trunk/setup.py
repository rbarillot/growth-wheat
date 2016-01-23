# -*- coding: latin-1 -*-
"""
Notes:

- use setup.py develop when tracking in-development code
- when removing modules or data files from the project, run setup.py clean --all and delete any obsolete .pyc or .pyo.

"""

"""
    Information about this versioned file:
        $LastChangedBy$
        $LastChangedDate$
        $LastChangedRevision$
        $URL$
        $Id$
"""

import ez_setup
ez_setup.use_setuptools()

import sys
from setuptools import setup, find_packages

import growthwheat

if sys.version_info < (2, 7):
    print('ERROR: Growth-Wheat requires at least Python 2.7 to run.')
    sys.exit(1)

if sys.version_info >= (3, 0):
    print('WARNING: Growth-Wheat has not been tested with Python 3.')

setup(
    name = "Growth-Wheat",
    version=growthwheat.__version__,
    packages = find_packages(),

    install_requires = ['numpy>=1.7.2', 'pandas>=0.14.0', 'scipy>=0.12.1', 'matplotlib>=1.3.1'],
    include_package_data = True,

    # metadata for upload to PyPI
    author = "C.Chambon, R.Barillot",
    author_email = "camille.chambon@grignon.inra.fr, romain.barillot@grignon.inra.fr",
    description = "Mechanistic model of wheat growth",
    long_description = "A mechanistic model for wheat that accounts for organ extension and growth according to the CN status",
    license = "", # TODO
    keywords = "", # TODO
    url = "https://sourcesup.renater.fr/projects/growth-wheat/",
    download_url = "", # TODO
)
