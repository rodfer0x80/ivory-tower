#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read Server header from response
# Return Server ID string


import sys, requests


def get_server_id(host):
    output = ""
    
    res = requests.get(f"http://{host}/")
    output = res.headers['Server']
    if output == "" or output == None:
        res = requests.post(f"http://{host}/")
        output = res.headers['Server']
        
    if output == "" or output == None:
        res = requests.get(f"https://{host}/")
        output = res.headers['server']
        
    if output == "" or output == None:
        res = requests.post(f"https://{host}/")
        output = res.headers['server']

    if output == "" or output == None:
        sys.stderr.write("[get_server_id] Failed to connect to server\n")
        exit(0)
    output += "\n" 
    with open('report/server_id.txt', 'w') as fp:
        fp.write(output)
    return output


if __name__ == '__main__':
    host = sys.argv[1]
    output = get_server_id(host)
    print(output)
    exit(0)
