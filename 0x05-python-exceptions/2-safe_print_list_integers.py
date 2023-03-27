#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    count_xelements = 0
    for i in range(x):
        if isinstance(my_list[i], int):
            try:
                print("{:d}".format(my_list[i]), end='')
                count_xelements += 1
            except (TypeError, IndexError):
                pass
    print()
    return(count_xelements)
