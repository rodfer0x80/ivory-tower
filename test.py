#!/usr/bin/python3


import os


if __name__ == '__main__':
    cmd = f'source {os.environ["PWD"]}/venv/bin/activate && testpy'
    os.system(cmd)
    exit(0)
