#!/usr/bin/env python

try:
    from setuptools import setup
except:
    from distutils.core import setup

setup(
    name='skkserv-lite',
    version='1.1',
    author='INAJIMA Daisuke',
    author_email='inajima@sopht.jp',
    description='SKK server using sqlite3 dictionaries',
    scripts=['skkserv-lite'],
    license='MIT',
)
