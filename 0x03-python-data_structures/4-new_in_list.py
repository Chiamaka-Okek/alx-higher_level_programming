#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    for number in range(len(my_list)):
        if idx < 0 and idx > number:
            return my_list
        else:
            y = []
            for x in my_list:
                y.append(x)
                y[idx] = element
                return(y)
