#!/usr/bin/python3
def uniq_add(my_list=[]):
    my_set = set(my_list)
    my_list = list(my_set)
    count = 0
    for x in range(len(my_list)):
        count = count + my_list[x]
    return count
