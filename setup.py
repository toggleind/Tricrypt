#!/usr/bin/env python

from setuptools import setup
from Tricrypt import __version__

setup(
    name = 'Tricrypt',
    packages = ['Tricrypt'],
    version =__version__,
    description = 'A secure, shoulder-surfing proof 2FA solution',
    license = 'AGPL',
    url = 'https://github.com/toggleind/tricrypt',
    entry_points = {
        'console_scripts': [
            'tricrypt = Tricrypt.__main__:main',
        ]
    },
    install_requires=['pyYAML']
)