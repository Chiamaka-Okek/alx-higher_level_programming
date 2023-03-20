#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
if __name__ == "__main__":
    operator = ['+', '-', '*', '/']
    number = len(argv) - 1
    if number != 3:
        print("Usage: ./100-mycalculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    c = add(a, b)
    d = sub(a, b)
    e = mul(a, b)
    f = div(a, b)
    if argv[2] == operator[0]:
        print("{} {} {} = {}".format(a, argv[2], b, c))
    elif argv[2] == operator[1]:
        print("{} {} {} = {}".format(a, argv[2], b, d))
    elif argv[2] == operator[2]:
        print("{} {} {} = {}".format(a, argv[2], b, e))
    elif argv[2] == operator[3]:
        print("{} {} {} = {}".format(a, argv[2], b, f)) 
    else:
        print("Unknown operator. Available operators: +, -, *, and /")
        exit(1) 
