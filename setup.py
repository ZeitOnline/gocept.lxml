# Copyright (c) 2007 gocept gmbh & co. kg
# See also LICENSE.txt
# $Id$

import os

from setuptools import setup, find_packages

setup(
    name = 'gocept.lxml',
    version = "0.3.0+lxml5",
    author = "Christian Zagrodnick",
    author_email = "cz@gocept.com",
    description = "Primarily provides zope3 interface definitions for lxml",
    long_description = open(os.path.join(
        os.path.dirname(__file__), 'src', 'gocept', 'lxml', 'README.txt')
        ).read(),
    license = "ZPL 2.1",
    url='https://console.cloud.google.com/artifacts/python/zeitonline-engineering/europe-west3/pypi-zon/gocept.lxml?project=zeitonline-engineering',

    packages = find_packages('src'),
    package_dir = {'': 'src'},

    include_package_data = True,
    zip_safe = False,

    namespace_packages = ['gocept'],
    install_requires = [
        'setuptools',
        'zope.interface',
        'zope.app.component',
        'lxml',
    ],
    extras_require = dict(
        test=['zope.testing',
              'zope.app.testing',
             ],
    ),
    )
