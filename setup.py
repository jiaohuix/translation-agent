# Copyright (c) Meta Platforms, Inc. and affiliates.
# This software may be used and distributed according to the terms of the GNU General Public License version 3.
import setuptools
from setuptools import setup, find_packages
from os import path

# this_directory = path.abspath(path.dirname(__file__))
# with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
#     long_description = f.read()

# setup(
#     name='translation_agent',
#     version='1.0',
#     packages=setuptools.find_packages(
#         where=".",
#         exclude=("examples*",),
#     ),
#     project_urls={
#         "Gitter": "https://github.com/jiaohuix/translation_agent",
#     },

#     install_requires=[
#         "zhipuai",
#     ],
# )
import re

def get_version() -> str:
    with open('translation_agent/__init__.py', encoding='utf-8') as f:
        version = re.search(
            r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
            f.read(),
            re.MULTILINE,
        ).group(1)
    return version


def read_requirements():
    with open('requirements.txt') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


def read_description() -> str:
    with open('README.md', 'r', encoding='UTF-8') as f:
        long_description = f.read()
    return long_description


setup(
    name='translation-agent',
    version=get_version(),
    author='jiaohui',
    author_email='',
    description='translation agent',
    long_description=read_description(),
    long_description_content_type='text/markdown',
    keywords=['LLM', 'Agent', 'Translation','Terminology', 'NMT'],
    packages=find_packages(exclude=['examples', 'examples.*']),
    install_requires=read_requirements(),
    # extras_require={
    #     'gui': [
    #         'gradio==4.21.0',
    #         'modelscope-studio>=0.4.0',
    #     ],
    # },
    url='https://github.com/jiaohuix/translation-agent.git',
)