#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if a_dictionary is not None and type(a_dictionary) is dict:
        dic_del = {i: j for i, j in a_dictionary.items() if j == value}
        for key, val in dic_del.items():
            del a_dictionary[key]
    return (a_dictionary.copy())
