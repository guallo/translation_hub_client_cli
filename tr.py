#!/usr/bin/python

import os
import sys
import socket

DEFAULT_HUB_ADDR = 'localhost:8091'


hub_addr = os.environ.get('HUB_ADDR', DEFAULT_HUB_ADDR)
hub_host = hub_addr.split(':')[0]
hub_port = int(hub_addr.split(':')[1])

# sending...
str_ = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((hub_host, hub_port))
s.sendall(str_ + '\0')

# receiving...
result = ''
while True:
    subresult = s.recv(4096)
    if not subresult:
        break
    result += subresult
s.close()

if sys.stdout.isatty():
    print result.decode('utf-8')  # let's python determine the right TTY's codec
else:
    print result  # utf-8 encoded
