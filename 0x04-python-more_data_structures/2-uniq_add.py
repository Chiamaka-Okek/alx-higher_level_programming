#!/usr/bin/python3
""" This function adds all unique integers in a list """


def uniq_add(my_list=[]):
    a = sum(set(my_list))
    return(a)
