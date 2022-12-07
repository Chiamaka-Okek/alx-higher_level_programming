#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    dic_sort = sorted(a_dictionary)
    for x in dic_sort:
        u = a_dictionary[x]
        print("{}: {}".format(x, u))
