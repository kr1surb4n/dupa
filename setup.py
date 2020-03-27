# -*- coding: utf-8 -*-
import io
import os
import re

from setuptools import find_packages
from setuptools import setup


def read(filename):
    filename = os.path.join(os.path.dirname(__file__), filename)
    text_type = type(u"")
    with io.open(filename, mode="r", encoding='utf-8') as fd:
        return re.sub(text_type(r':[a-z]+:`~?(.*?)`'), text_type(r'``\1``'), fd.read())


flake8_entry_point = "flake8.extension"

setup(
    name="dupa",
    version="0.1.4",
    url="https://github.com/kr1surb4n/dupa",
    license='MIT',

    author="Kris Urbanski",
    author_email="kris@whereibend.space",

    description="Dupa - set of tools handy during debuging.",
    long_description=read("README.md"),
    long_description_content_type="text/markdown",

    packages=find_packages(exclude=('tests', 'docs',)),

    install_requires=['flake8'],
    entry_points={
                flake8_entry_point: [
                    'X8083 = flake8_dupa_check:Check4Dupa',
                ],
    },
    tests_require=["pytest"],
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
