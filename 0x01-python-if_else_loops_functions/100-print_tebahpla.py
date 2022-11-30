#!/usr/bin/python3
for x in range(122, 96, -1):
    if x % 10 % 2 != 0:
        x -= 32
    else:
        x
    print("{:c}".format(x), end='')
