#!/usr/bin/python3
""" This function returns the key with the biggest integer value """


def best_score(a_dictionary):
    """ Return an integer """
    if a_dictionary is None:
        return(None)
    else:
        max_y = max(a_dictionary.values())
        for x, y in a dictionary.items():
            if a_dictionary[x] == max_y:
                return(x)
