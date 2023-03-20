#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    elements = dir(hidden_4)
    for x in elements:
        if x[:2] != '__':
            print(x)
