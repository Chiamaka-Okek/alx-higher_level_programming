#!/usr/bin/python3
def search_replace(my_list, search, replace):
    new_list = my_list.copy()
    for y in range(len(my_list)):
        if new_list[y] == search:
            new_list[y] = replace
    return new_list
