# -*- coding: utf-8 -*-
"""Run the project"""

import os
import sys
import subprocess

base_dir = os.path.dirname(os.path.abspath(__file__))


def current():
    """Run the project with current environment"""
    package = ' * Module <{}> is not found. Would you like to pip install it? (y/n) '
    failure = '\n * Failed to run the project.\n'
    fulfill = ' * All required modules are found.'

    with open(base_dir + '/requirements.txt') as r:
        module_list = [m.split('==')[0].lower() for m in r.readlines()]

    from pip import get_installed_distributions as gid
    module_list_exist = [m.key for m in gid()]
    module_list_required = sorted(list(set(module_list) - set(module_list_exist)))

    for m in module_list_required:
        while True:
            command = input(package.format(m))
            if command not in ['y', 'n']:
                print('Invalid Input.')
            else:
                break
        if command == 'y':
            interpreter_dir = sys.executable.rsplit('/', 1)[0]
            os.system('{}/pip3 install {}'.format(interpreter_dir, m))
        else:
            print(failure)
            exit()

    print(fulfill)
    python_bin = sys.executable
    run(python_bin=python_bin)


def virtual():
    """Run the project with virtual environment"""
    prepare = ' * Preparing virtual environment...'
    ve_done = ' * Virtual environment is created.'
    existed = ' * Existing virtual environment is found. Use it? (y/n) '

    if not os.path.isdir(base_dir + '/venv'):
        print(prepare)
        os.system('cd ' + base_dir)
        os.system('virtualenv venv')
        for package in ['flask', 'plotly', 'requests', 'bs4']:
            os.system('{}/venv/bin/pip3 install {}'.format(base_dir, package))
        print(ve_done)

    else:
        while True:
            command = input(existed)
            if command not in ['y', 'n']:
                print('Invalid Input.')
            else:
                break
        if command == 'n':
            os.system('rm -rf {}'.format(base_dir + '/venv'))
            print(prepare)
            os.system('cd ' + base_dir)
            os.system('virtualenv venv')
            for package in ['flask', 'plotly', 'requests', 'bs4']:
                os.system('{}/venv/bin/pip3 install {}'.format(base_dir, package))
            print(ve_done)

    python_bin = base_dir + '/venv/bin/python3'
    run(python_bin=python_bin)


def run(python_bin):
    """Run setup.py"""
    welcome = ' * Try running the project...'
    process = ' * Press CTRL+C to quit.\n'
    goodbye = '\n * The project is shut down.\n'

    print(welcome)
    script_file = base_dir + '/setup.py'
    sub = subprocess.Popen([python_bin, script_file])

    try:
        nothing = input('')
        while True:
            nothing = input(process)
    except (KeyboardInterrupt, SystemExit):
        print(goodbye)
        sub.terminate()


if __name__ == '__main__':
    while True:
        response = input('Run the project under: (1/2)\n1. Current environment\n2. Virtual environment\n')
        if response not in ['1', '2']:
            print('Invalid Input.')
        else:
            break

    if response == '1':
        current()
    else:
        virtual()
