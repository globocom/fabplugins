#!/usr/bin/env python
# -*- coding: utf-8 -*-


from setuptools import setup

version = '1.0.1'

setup(
    name='fabplugins',
    version=version,
    description="Fabric plugins",
    long_description="Fabric plugins",
    keywords='fabplugins',
    author='Time Home',
    author_email='timehome@corp.globo.com',
    url='',
    license='MIT',
    classifiers=[],
    packages=['fabplugins'],
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        "fabric"
    ]
)
