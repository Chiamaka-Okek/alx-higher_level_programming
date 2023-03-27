#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count_xelement = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end='')
            count_xelement += 1
        except IndexError:
            break
    print()
    return(count_xelement)
