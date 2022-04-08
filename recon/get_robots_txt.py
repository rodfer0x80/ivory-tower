#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read robots.txt
# Parse and sort data to enumerate sitemap
# Return string of sitemap entries newline separated


import sys, requests


def get_robots_txt(host):
    output = ""

    try:
        res = requests.get(f"http://{host}/robots.txt")
        if res.status_code != 200:
            res = requests.get(f"https://{host}/robots.txt")
            if res.status_code != 200:
                output = res.text
            else:
                sys.stderr.write("[get_robot_txt] Failed to connect to server\n")
                exit(0)
        else:
            output = res.text
        
    except Exception as e:
        sys.stderr.write(f"[get_robot_txt] Network connection error: {e}\n")
        exit(1)
    with open('report/robots.txt', 'w') as fp:
        fp.write(output)
    return output


if __name__ == '__main__':
    host = False
    host = sys.argv[1]
    output = get_robot_txt(host)
    print(output)
    exit(0)
