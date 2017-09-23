#!/usr/bin/env python
import subprocess

import utils

dest_addr = "10.0.0.1"
open_seq = [1234, 4321, 2341]
open_command = "ssh  10.0.0.1 22"


def main():
    for i in open_seq:
        utils.knock(dest_addr, i)
    subprocess.call(open_command, shell=True)


if __name__ == '__main__':
    main()
