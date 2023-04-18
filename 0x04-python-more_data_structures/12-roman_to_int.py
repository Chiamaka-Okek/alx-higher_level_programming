#!/usr/bin/python3
""" This function Roman numeral to an integer """


def roman_to_int(roman_string):
    """ Returns an integer after conversion """
    sum_num = 0
    my_list = []
    my_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    for x, y in my_dict.items():
        for z in roman_string:
            if z == x:
                my_list.append(y)
            b = sum(my_list)
        return(b)
