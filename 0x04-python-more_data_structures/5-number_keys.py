#!/usr/bin/python3
def number_keys(a_dictionary):
    count = 0
    for x in range(len(list(a_dictionary))):
        count = count + x
    return count
