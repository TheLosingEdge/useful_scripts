#!/usr/bin/env python3
"""Resolve hostnames from a file into their IP addresses."""

import socket
import sys


def main() -> None:
    print()
    filename = input("Enter input file> ")

    try:
        infile = open(filename)
    except OSError as e:
        print(e)
        sys.exit(1)

    print(f"\nFile {filename} exists!")
    print("\nGetting IP addresses for hosts\n")

    for line in infile:
        hostname = line.strip()
        try:
            ipaddr = socket.gethostbyname(hostname)
            print(ipaddr)
        except socket.gaierror as e:
            print(f"Couldn't find IP address for {hostname}: {e}")
            continue

    infile.close()
    print("\nFinished the operation")


if __name__ == "__main__":
    main()
