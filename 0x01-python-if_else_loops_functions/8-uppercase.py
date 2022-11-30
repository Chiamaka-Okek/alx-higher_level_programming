#!/usr/bin/python3
def uppercase(str):
    for x in str:
        ch = ord(x)
        if ch >= 97 or ch <= 122:
            print(chr(ch))
    print("\n")
