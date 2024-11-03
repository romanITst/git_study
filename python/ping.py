#! /usr/bin/env python3

import subprocess

host = input("Enter the ip address or hostname.com to ping: ")

result = subprocess.run(["ping", "-c", "5", f"{host}"])

if result.returncode == 0:
    print("success")
else:
    print("doesn't work")
