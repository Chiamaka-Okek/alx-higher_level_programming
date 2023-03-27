#!/usr/bin/python3
def safe_print_integer(value):
    if isinstance(value, int):
        try:
            print("{:d}".format(value, end=""))
            return(True)
        except (TypeError, ValueError):
            return(False)
