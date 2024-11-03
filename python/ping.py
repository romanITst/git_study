#! /usr/bin/env python3

import os

ip_addr = str(input("Enter the address to ping: "))
count = str(input("Enter the times of ping: "))

print(os.popen(f"ping {ip_addr} -c {count}").read())