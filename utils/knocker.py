#!/usr/bin/env python
import socket
import subprocess

h = "10.0.0.1"
o = 1234
t = 4321
w = 2341
c = "telnet 10.0.0.1 8888"


def knock(host, port):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        skt.connect((host, port))
        skt.shutdown(2)
        return True
    except socket.error:
        return False


def main():
    s1, s2, s3, s4, s5, s6 = [o, t, w], [o, w, t], [t, w, o], [t, o, w], [w, o, t], [w, t, o]

    for i in s6:
        knock(h, i)
    subprocess.call(c, shell=True)


if __name__ == '__main__':
    main()
