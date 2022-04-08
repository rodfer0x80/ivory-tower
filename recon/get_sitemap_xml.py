#!/usr/bin/python3


# Send GET and POST request trying HTTPS and HTTP 
# Read sitemap.xml 
# Parse and sort data to enumerate sitemap
# Return string of sitemap entries newline separated


import sys, requests


def get_sitemap_xml(host):
    output = ""

    try:
        res = requests.get(f"http://{host}/sitemap.xml")
        output = res.status_code
    
        if res.status_code != 200:
            res = requests.get(f"https://{host}/sitemap.xml")
        
            if res.status_code != 200:
                output = res.text
            else:
                sys.stderr.write("[get_sitemap_xml] Failed to connect to server\n")
                exit(0)
        else:
            output = res.text
        
    except Exception as e:
        sys.stderr.write(f"[get_sitemap_xml] Network connection error: e\n")
        exit(1)
    
    with open('report/sitemap.xml', 'w') as fp:
        fp.write(output)
    return output


if __name__ == '__main__':
    host = False
    host = sys.argv[1]
    sys.stderr.write("Usage: ./get_sitemap_xml.py <host>\n")
    output = get_sitemap_xml(host)
    print(output)
    exit(0)
