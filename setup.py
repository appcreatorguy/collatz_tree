#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = ['Click>=7.0', ]

setup(
    author="Manas Mengle",
    author_email='appcreatorguy@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    description="A simple CLI app for generating a Collatz Tree",
    entry_points={
        'console_scripts': [
            'collatz_tree=collatz_tree.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='collatz_tree',
    name='collatz_tree',
    packages=find_packages(include=['collatz_tree', 'collatz_tree.*']),
    url='https://github.com/appcreatorguy/collatz_tree',
    version='0.1.0',
    zip_safe=False,
)
