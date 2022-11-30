#!/usr/bin/python3
def uppercase(str):
    for x in str:
        ch = ord(x)
        if ch >= 97 and ch <= 122:
            ch = ch - 32
            print("{}".format(chr(ch)), end='')
    print("\n")
