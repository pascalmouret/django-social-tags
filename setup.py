# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

import os


APP = 'social_tags'
VERSION = __import__(APP).__version__
AUTHOR = 'Pascal Mouret'
NAME = 'django-social-tags'
URL = 'https://github.com/pascalmouret/django-social'
AUTHOR_MAIL = 'pascal.mouret@divio.ch'
DESCRIPTION = 'Social meta-tag handler for Django.'
README = 'README.md'

REQUIREMENTS = [
	'django-sekizai',
]

CLASSIFIERS = [
    'Environment :: Web Environment',
    'Framework :: Django',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: BSD License',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
    ]

# make it work
if not 'a' in VERSION and not 'b' in VERSION: CLASSIFIERS.append('Development Status :: 5 - Production/Stable')
elif 'a' in VERSION: CLASSIFIERS.append('Development Status :: 3 - Alpha')
elif 'b' in VERSION: CLASSIFIERS.append('Development Status :: 4 - Beta')

def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name=NAME,
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_MAIL,
    description=DESCRIPTION,
    long_description=read(README),
    url=URL,
    classifiers=CLASSIFIERS,
    platforms=['OS Independent'],
    install_requires=REQUIREMENTS,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False
)