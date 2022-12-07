#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = a_dictionary.copy()
    for key, value in new.items():
        value = value * 2
        new[key] = value
    return new
