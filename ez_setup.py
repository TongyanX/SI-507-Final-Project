# -*- coding: utf-8 -*-
"""Easy Setup"""

import os
import subprocess


if __name__ == '__main__':
    welcome = ' * Try running the project...'
    process = ' * Press CTRL+C to quit.\n'
    goodbye = '\n * The project is shut down.\n'

    base_dir = os.path.dirname(os.path.abspath(__file__))
    python_bin = base_dir + '/venv/bin/python3.6'
    script_file = base_dir + '/setup.py'

    print(welcome)
    sub = subprocess.Popen([python_bin, script_file])

    try:
        nothing = input('')
        while True:
            nothing = input(process)
    except (KeyboardInterrupt, SystemExit):
        print(goodbye)
        sub.terminate()
