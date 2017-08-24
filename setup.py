from setuptools import setup
from os import path

import eph

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.rst')) as f:
    long_description = f.read()

setup(
    name=eph.__project__,
    version=eph.__release__,
    description='Retrieve and manipulate Jpl Horizons Ephemerides.',
    long_description=long_description,
    author=eph.__author__,
    author_email='flavio.grandin@gmail.com',
    install_requires=[
        'requests',
        'astropy',
    ],
    include_package_data=True,
    license='MIT',
    url='https://github.com/bluePhlavio/eph',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Astronomy',
        'Topic :: Scientific/Engineering :: Physics',
        'Programming Language :: Python :: 3.4',
        ],
    keywords='jpl horizons ephemeris astronomy planets',
    packages=['eph'],
    entry_points={
        'console_scripts': ['eph=eph.__main__:main'],
    },
)
