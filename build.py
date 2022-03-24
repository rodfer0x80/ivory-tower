#!/usr/bin/python3


import os


if __name__ == '__main__':
    cmd =  'virtualenv "$PWD/venv" &&\
            source "$PWD/venv/bin/activate" &&\
            pip install . && pip install pytest &&\
            exit 0' 
    os.system(cmd)
    print(f'source {os.environ["PWD"]}/venv/bin/activate')
    exit(0)
