import codecs
import os
import re

from setuptools import setup

here = os.path.abspath(os.path.dirname(__file__))


def read(*parts):
    # intentionally *not* adding an encoding option to open
    return codecs.open(os.path.join(here, *parts), 'r').read()


def find_version(*file_paths):
    version_file = read(*file_paths)
    version_match = re.search(r"^__version__ = ['\"]([^'\"]*)['\"]",
                              version_file, re.M)
    if version_match:
        return version_match.group(1)
    raise RuntimeError("Unable to find version string.")


long_description = read('README.md')


setup(
    # i.e. `pip install xboxapi`
    name='xboxapi',
    version=find_version('xboxapi', '__init__.py'),
    url='https://github.com/xboxapi/Python-Wrapper',
    license='MIT License',
    author='XBoxApi.com',
    install_requires=['requests',
                      ],
    #author_email='',
    description='XBOX One API',
    long_description=long_description,
    packages=['xboxapi'],
    package_data={'': ['REDAME.md', 'LICENSE']},
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
