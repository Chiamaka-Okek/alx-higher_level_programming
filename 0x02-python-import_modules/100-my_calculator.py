#!/usr/bin/python3
from calculator_1 import add, sub, mul, div
from sys import argv
operator = ['+', '-', '*', '/']
c = add(a, b)
d = sub(a, b)
e = mul(a, b)
f = div(a, b)
for number in len(argv):
    if number != 3:
        print("Usage: ./100-mycalculator.py <a> <operator> <b>\n")
        exit 1
        for x in operator:
            if number == 3 and x != operator:
                print("Unknown operator. Available operators: +, -, *, and /")
                exit 1
            else:
                print("{}" + "{}" + "{}" = "{}".format(a, b, str(argv[2]), c))
                print("{}" + "{}" + "{}" = "{}".format(a, b, str(argv[2]), d))
                print("{}" + "{}" + "{}" = "{}".format(a, b, str(argv[2]), e))
                print("{}" + "{}" + "{}" = "{}".format(a, b, str(argv[2]), f))
