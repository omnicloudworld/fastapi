#!/usr/bin/env python3
#-*- coding:utf-8 -*- # noqa: E265
'''
Script for install package localy.
'''

# import argparse
from subprocess import (
    run, PIPE
)
from os import (
    environ as env,
    path, remove, rename
)
from pathlib import Path
from shutil import rmtree, copyfile
import yaml


# pylint: disable=missing-docstring
def install_local():

    env['CI_PIPELINE_IID'] = '0'
    env['BUILD_SUFIX'] = '.dev'

    try:

        build_run = run(
            'python3 -m build --no-isolation ./pypi',
            check=False,
            shell=True,
            text=True,
            stderr=PIPE
        )
        if build_run.returncode != 0:
            raise RuntimeError(build_run.stderr)

        install_run = run(
            ''.join(
                [
                    'pip3 install --force-reinstall --no-build-isolation --user ./pypi/dist/',
                    f'{conf["NAMESPACE"].replace(".", "-")}-{conf["VERSION"]}.dev0.tar.gz; ',
                    f'rm -dfR {path.join(path.dirname(path.realpath(__file__)), "pypi/dist")}'
                ]
            ),
            check=False,
            shell=True,
            text=True,
            stderr=PIPE
        )
        if install_run.returncode != 0:
            raise RuntimeError(install_run.stderr)

    finally:

        rmtree(f'pypi/src/{conf["NAMESPACE"].replace(".", "_")}.egg-info')
        if Path('README.md').is_file():
            remove('pypi/README.md')
            if README_EXISTS:
                rename('pypi/README.bak', 'pypi/README.md')


if __name__ == '__main__':

    with open('./pypi/env.yml', 'r', encoding='utf-8') as vars_file:
        conf = yaml.safe_load(vars_file)

    README_EXISTS = Path('pypi/README.md').is_file()

    if Path('README.md').is_file():
        if README_EXISTS:
            rename('pypi/README.md', 'pypi/README.bak',)
        copyfile('README.md', 'pypi/README.md')

    install_local()
