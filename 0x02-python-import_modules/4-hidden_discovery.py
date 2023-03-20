#!/usr/bin/python3
if __name__ == "__main__":
    elements = hidden_4.pyc.split()
    for x in elements:
        if x[0] == '_':
            exit(1)
        else:
            print(x)
