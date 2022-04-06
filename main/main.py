import sys
import os
import time
import subprocess
import random

import configs 

class Logger:
    def __init__(self):
        self.logger_path = f"{os.environ['PWD']}/ivory-tower_cluster.log"
        _ = subprocess.call(f"touch {self.logger_path}".split())

    def write(self, data: str):
        try:
            with open(self.logger_path, 'a') as fo:
                fo.write(data)
        except Exception as e:
            print(e)
        return 0
    

class Cluster():
    def __init__(self):
        self.instances = list()
        self.logger = Logger()
        return None

#    def launch_cluster(self):
#        for i in range(len(self.instances)):
#            self.logger.write(f"Launched cluster {i}")
#        return 0


    def start_instance(self):
        instance_id = ""
        alphabet = "0123456789abcdef"
        time.sleep(2)
        instance_id = ''.join([random.choice(alphabet) for i in range(16)])
        self.instances.append(instance_id)
        self.logger.write(f"Instance {instance_id} started\n")
        return instance_id
    
    def run_instance(self, cmd: str):
        docker_cmd = f"docker run -d --rm alpine:7 -c / 'bin/bash {cmd}' --volume ./subdomains:/subdomains"
        self.logger.write(f'{docker_cmd}\n')
        return 0

    def stop_instance(self, instance_id):
        tmp_instances = []
        for instance in self.instances:
            if instance_id != instance:
                tmp_instances.append(instance)
        self.instances = tmp_instances
        self.logger.write(f"Instance {instance_id} stopped\n")
        return 0

    def instance_run_once_then_die(self, cmd: str):
        instance_id = self.start_instance()
        self.run_instance(cmd)
        self.stop_instance(instance_id)
        return 0


    def system_run(self, cmd: str):
        self.logger.write(f'{cmd}\n')
        with open('sys_run.sh', 'w') as fo:
            fo.write(f"#!/bin/bash\n{cmd}")
        os.system("bash sys_run.sh")
        os.system("rm sys_run.sh")
        return 0

def main():
    ls = os.listdir()
    if "subdomains" not in ls:
        os.mkdir(subdomains)
    domain = "example.com"
    #domain = input("[+] Domain name\n>>> ")
    
    cmds = configs.parse_cmds(domain)
    cleanup = cmds.pop()

    cluster = Cluster()

    for cmd in cmds:
        cluster.instance_run_once_then_die(cmd)
    while len(cluster.instances) > 0:
        time.sleep(3)
        print(cluster.instances)
    cluster.system_run(cleanup)
    return 0

if __name__ == '__main__':
    exit(main())

