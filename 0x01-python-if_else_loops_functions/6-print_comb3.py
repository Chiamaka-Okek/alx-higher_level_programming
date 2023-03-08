#!/usr/bin/python3
for x in range(0, 10):
    for y in range(0, 10):
        if x <= 7 and x != y and y > x:
            print("{}{}, ".format(x, y), end='')
        elif x > 7 and x != y and y > x:
            print("{}{}".format(x, y), end='')
print()
