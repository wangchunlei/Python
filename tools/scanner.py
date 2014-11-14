#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from errno import ECONNREFUSED
from functools import partial
from multiprocessing import Pool
import socket
import subprocess

NUM_CORES = 3000


def ping(host, port):
    try:
        s = socket.socket()
        s.settimeout(1)
        s.connect((host, port))
        print str(port) + " Open"
        return port
    except socket.error as err:
        if err.errno == ECONNREFUSED:
            return False
        #$raise


def scan_ports(host):
    p = Pool(NUM_CORES)
    ping_host = partial(ping, host)
    return filter(bool, p.map(ping_host, range(1, 9999)))


def main(host=None):
    if host is None:
        host = "127.0.0.1"
    ports = list(scan_ports(host))
    print "\nDone."

    print str(len(ports)) + " ports available."
    print ports


if __name__ == '__main__':
	# Clear the screen
	subprocess.call('clear', shell=True)
	target = raw_input('Enter host to scan: ')
	print "-" * 60
	print "Please wait, scanning remote host", target
	print "-" * 60
	main(target)