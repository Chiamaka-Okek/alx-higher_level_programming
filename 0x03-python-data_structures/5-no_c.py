#!/usr/bin/python3
def no_c(my_string):
    empty_string =""
    for x in my_string:
        if x != 'c' and x != 'C':
            empty_string += x
        return(empty_string)
