#!/usr/bin/env python
# -*- coding: utf-8 -*-


import os
from setuptools import setup


def readfile(file_name):
    f = open(os.path.join(os.path.dirname(__file__), file_name))
    return f.read()


setup(
    name='ustudio-tornado-cors',
    version='0.7.0',
    description='CORS support for Tornado (uStudio Fork)',
    keywords='tornado cors',
    author='globo.com',
    author_email='guilherme.cirne@corp.globo.com',
    maintainer='ustudio.com',
    maintainer_email='dev@ustudio.com',
    url='https://github.com/ustudio/tornado-cors',
    license = 'MIT',
    classifiers = ['Development Status :: 4 - Beta',
                   'Intended Audience :: Developers',
                   'License :: OSI Approved :: MIT License',
                   'Natural Language :: English',
                   'Operating System :: MacOS',
                   'Operating System :: POSIX :: Linux',
                   'Programming Language :: Python :: 3.9',
                   'Topic :: Software Development :: Libraries',
    ],
    include_package_data=True,
    packages = ['tornado_cors'],
    install_requires=[requirement for requirement in readfile('requirements.txt').split('\n') if requirement],
)
