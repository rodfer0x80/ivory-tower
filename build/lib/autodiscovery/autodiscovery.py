import threading
import sys
import os
import time

from recon.get_robots_txt import get_robots_txt
from recon.get_sitemap_xml import get_sitemap_xml
from recon.get_server_id import get_server_id
from recon.get_favicon_framework import get_favicon_framework


class Threadpool:
    def __init__(self, host):
        self.host = host

    def start_timer(self):
        self.start = time.time()


    def get_time_elapsed(self):
        if self.start:
            finish = time.time()
            time_elapsed = finish - self.start
            del self.start
            return "%.2f seconds" % time_elapsed
        else:
            sys.stderr.write("[get_time_elapsed] Timer was not started\n")
            return "n/a"

    
    def run_threads(self, n_threads=4):
        # create n number of threads with a list of function calls
        # and run then in parallel
        self.threads = list()
        self.n_threads = n_threads
        for i in range(0, n_threads):
            if i == 0:
                self.threads.append(threading.Thread(target=get_robots_txt, args=(self.host,)))
            elif i == 2:
                self.threads.append(threading.Thread(target=get_favicon_framework, args=(self.host,)))
            elif i == 3:
                self.threads.append(threading.Thread(target=get_server_id, args=(self.host,)))
            else:
                self.threads.append(threading.Thread(target=get_sitemap_xml, args=(self.host,)))
            self.threads[i].start()
            self.threads[i].join()
        #parser.build_report()
        return 0


    def thread_log_data(self, data):
        self.mutex.write(data)
        return 0
    



def build_report_dir():
    if os.path.exists('report'):
        t = "%6.f" % time.time()
        try:
            os.rename('report', f'report_{t}')
        except Exception as e:
            sys.stderr.write(f"[!] Error moving old report: {e}")
            exit(1)
    try:
        os.mkdir('report')
    except Exception as e:
        os.umask(660)
        sys.stderr.write(f"[!] Error creating directory report: {e}")
        exit(1)


def run(host: str):
    build_report_dir()
    threadpool = Threadpool(host)
    threadpool.start_timer()
    threadpool.run_threads()
    if threadpool.run_threads() == 0:
        time_elapsed = threadpool.get_time_elapsed()
        print(f"[*] Report build in {time_elapsed} and saved to ./report ")
    exit(0)



