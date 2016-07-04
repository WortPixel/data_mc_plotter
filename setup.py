#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

config = {
    'description': 'Module for data-mccomparison with visualization suggested\
            by Aggerwal',
    'author': 'Mathis Börner',
    'url': 'https://github.com/mbrner/data_mc_plotter',
    'download_url': 'https://github.com/mbrner/data_mc_plotter/archive/master.zip',
    'author_email': 'mathis.boerner@tu-dortmund.de',
    'version': '0.1',
    'install_requires': [
        'matplotlib',
        'numpy',
        'scipy',
        'tables',
        'tqdm',
    ],
    'packages': [
        'data_mc_plotter',
        'data_mc_plotter.scripts',
    ],
    'name': 'data_mc_plotter'
}

setup(**config)
