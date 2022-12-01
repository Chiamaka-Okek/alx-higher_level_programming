#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    if len(argv) == 1:
        print((len(argv) - 1), "arguments.")
    elif len(argv) > 2:
        print((len(argv) - 1), "arguments:")
        for x in range(1, (len(argv))):
            str1 = str(x) + ": " + str(argv[x])
            print(str1)
    elif len(argv) == 2:
        print((len(argv) - 1), "argument:")
        str2 = str((len(argv) - 1)) + ": " + str(argv[1]) 
        print(str2)
print()
