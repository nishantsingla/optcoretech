# -*- coding: utf-8 -*-
#!/usr/bin/env python

import os
import sys

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

import optcoretech
version = optcoretech.__version__

setup(
    name='optcoretech-web',
    version=version,
    author='',
    author_email='sheeshmohsin@gmail.com',
    packages = [
	'optcoretech',
    ],
    include_package_data=True,
    install_requires=[
	'Django>=1.6.1',
    ],
    zip_safe=False,
    scripts=['optcoretech/manage.py'],
)

