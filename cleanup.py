#!/usr/bin/python3


import os


if __name__ == '__main__':
    pwd = os.environ["PWD"]
    cmd = f'rm -rf {pwd}/build {pwd}/venv {pwd}/ivory_tower.egg-info'
    os.system(cmd)
    exit(0)
