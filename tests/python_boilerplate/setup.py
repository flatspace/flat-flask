#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pip

from pip.req import parse_requirements

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup


with open('README.md') as readme_file:
    readme = readme_file.read()

with open('HISTORY.md') as history_file:
    history = history_file.read().replace('.. :changelog:', '')

parsed_requirements = parse_requirements(
    'requirements/prod.txt',
    session=pip.download.PipSession()
)

parsed_test_requirements = parse_requirements(
    'requirements/test.txt',
    session=pip.download.PipSession()
)


requirements = [str(ir.req) for ir in parsed_requirements]
test_requirements = [str(tr.req) for tr in parsed_test_requirements]


setup(
    name='python_boilerplate',
    version='0.0.1',
    description="",
    long_description=readme + '\n\n' + history,
    author="Joe Funnypants",
    author_email='something@something',
    url='https://github.com/flatspace/python_boilerplate',
    packages=[
        'python_boilerplate',
    ],
    package_dir={'python_boilerplate':
                 'python_boilerplate'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    keywords='python_boilerplate',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    test_suite='tests',
    tests_require=test_requirements
)
