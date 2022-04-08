#\!/usr/bin/python3

import sys
import os
import time

from lib.threadpool import Threadpool


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


def get_args():
    if len(sys.argv) != 2:
        sys.stderr.write("Usage:/ python3 __main__.py <host>\n")
        exit(1)
    host = sys.argv[1]
    return host


def bootstrap():
    host = get_args()
    build_report_dir()
    threadpool = Threadpool(host)
    threadpool.start_timer()
    threadpool.run_threads()
    if threadpool.run_threads() == 0:
        time_elapsed = threadpool.get_time_elapsed()
        print(f"[*] Report build in {time_elapsed} and saved to ./report ")
    exit(0)


if __name__ == '__main__':
    bootstrap()


