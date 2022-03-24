import os
import sys


################################################
# read configs from file $PWD/configs.txt
# extract and build list of commands
# read domain from cli args
# format commands to call
# returns list of ready to execute cmds 
################################################


def read_configs() -> str:
    CONFIGS_PATH = f'{os.environ["PWD"]}/configs/configs.txt'
    
    configs = ''
    with open(CONFIGS_PATH, 'r') as fi:
        configs += fi.read()
    
    return configs


def parse_configs() -> str:
    configs = read_configs().strip().splitlines()
    
    cmds = ''
    i = 0
    for line in configs:
        if "cmd" in line:
            cmds += f'{configs[i+1].strip()}\n'
        i += 1
    
    return cmds[:-1].splitlines()


def parse_args() -> str:
    if len(sys.argv) != 2:
        sys.stderr.write('parse_args: invalid length\n')
        exit(1)
    
    return sys.argv[1]


def parse_cmds() -> str:
    cmds = parse_configs()
    domain = parse_args()
    
    _cmds = list()
    for cmd in cmds:
        cmd = cmd.replace('$domain', domain)
        cmd = cmd.replace('$rsrc', domain)
        _cmds.append(cmd)
    return _cmds

