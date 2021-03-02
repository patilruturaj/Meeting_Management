# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in meeting_management/__init__.py
from meeting_management import __version__ as version

setup(
	name='meeting_management',
	version=version,
	description='This is Meeting management App ',
	author='Ruturaj Patil',
	author_email='ruturaj@example.com',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
