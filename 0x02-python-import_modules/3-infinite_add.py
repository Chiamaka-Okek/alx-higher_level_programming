#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    y = 0
    for x in range(1, len(argv)):
        y = y + int(argv[x])
    print("{}".format(y))
