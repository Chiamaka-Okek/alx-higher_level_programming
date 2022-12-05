#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    number = len(my_list)
    if idx < 0 or idx >= number:
        return my_list
    else:
        y = []
        for x in my_list:
            y.append(x)
        y[idx] = element
        return(y)
