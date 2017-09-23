#!/usr/bin/env python
import datetime

import utils

h = "ya.ru"  # host to scan
pf = 75  # first port to scan
pt = 85  # last port to scan


def main():
    st = datetime.datetime.now()

    print("Scan for ports from " + str(pf) + " to " + str(pt) + " for " + h + " started at " + str(st) + "\n")
    for i in range(pf, pt):
        if utils.knock(h, i):
            print("\tPort " + str(i) + " is open.")

    print("\n")
    et = datetime.datetime.now()

    print("Scan ended at: " + str(et))


if __name__ == '__main__':
    main()
