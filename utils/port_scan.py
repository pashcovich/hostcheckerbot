#!/usr/bin/env python
import socket
import subprocess
import datetime

h = "127.0.0.1"
pf = 1
pt = 50


def knock(host, port):
    skt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        skt.connect((host, port))
        skt.shutdown(2)
        return True
    except socket.error:
        return False


def main():
    st = datetime.datetime.now()

    print("Scan for ports from " + str(pf) + " to " + str(pt) + " for " + h + " started at " + str(st))
    for i in range(pf, pt):
        if knock(h, i):
            print("Port " + str(i) + " is open.")

    et = datetime.datetime.now()

    print("Scan done  in: " + str(et.time - st.time))

if __name__ == '__main__':
    main()
