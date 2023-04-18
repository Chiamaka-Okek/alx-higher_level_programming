#!/usr/bin/python3
""" This function replaces all occurrence of an element by
another new list """


def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for x in range(len(new_list)):
        if new_list[x] == search:
            new_list[x] = replace
    return(new_list)
