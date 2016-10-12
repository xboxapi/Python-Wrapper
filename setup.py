import codecs
import os
import re

import xboxapi

from setuptools import setup

bin = os.path.abspath(os.path.dirname(__file__))

def read(file):
    return codecs.open(os.path.join(bin, file), 'r').read()

long_description = read('README.md')

setup(
    name='xboxapi',
    version=xboxapi.__version__,
    url='https://github.com/xboxapi/Python-Wrapper',
    license='MIT License',
    author='xboxapi.com',
    install_requires=['requests'],
    description='XBOX One API',
    long_description=long_description,
    packages=['xboxapi'],
    package_data={'': ['README.md', 'LICENSE']},
    include_package_data=True,
    platforms='any',
    classifiers=[
        'Programming Language :: Python',
        'Development Status :: 3 - Alpha',
        'Natural Language :: English',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Topic :: Games/Entertainment',
        ],
)
