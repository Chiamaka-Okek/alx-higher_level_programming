#!/usr/bin/pyhton3
def replace_in_list(my_list, idx, element):
    number = len(my_list)
    if idx < 0 or idx >= number:
        return my_list
    else:
        my_list[idx] = elemnt
        return my_list
