#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages
import labyrinth
 
with open('requirements.txt') as f:
    requires = f.read().split('\n')

setup(

    name='oc-labyrinth',
    version=3.2,
 
    packages=find_packages(),
    install_requires=requires,
    author='Nico Zhan',
    author_email='nicozhan@hyperloop.fr',
    description='Help Mc Gyver to leave the maze',
    long_description=open('README.md').read(),

    # include file from manifest.in
    include_package_data=True,
    url='https://github.com/Hyperyon/p3-labyrinthe',
    classifiers=[
        'Programming Language :: Python',
        'Operating System :: OS Independent',
        'Programming Language :: Python :: 3.5',
        'Topic :: Game',
    ],
 
)