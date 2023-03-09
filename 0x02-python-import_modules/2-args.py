#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print("{} arguments.".format(len(argv) - 1))
    elif len(argv) > 2:
        print("{} arguments: ".format(len(argv) - 1))
        for x in range(1, (len(argv))):
            str1 = str(x) + ": " + str(argv[x])
            print("{}".format(str1))
    elif len(argv) == 2:
        print("{} argument:".format(len(argv) - 1))
        str2 = str(len(argv) - 1) + ": " + str(argv[1])
        print("{}".format(str2))
