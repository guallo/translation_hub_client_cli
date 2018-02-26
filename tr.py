#!/usr/bin/python

import sys
import socket


# sending...
str_ = sys.argv[1]
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('localhost', 8090))
s.sendall(str_ + '\0')

# receiving...
result = ''
while True:
    subresult = s.recv(4096)
    if not subresult:
        break
    result += subresult
s.close()

print result.decode('utf-8')
