#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary == None:
        return
    score = []
    for key, value in a_dictionary.items():
        score.append(value)
        score.sort()
        for x in a_dictionary:
            if a_dictionary[x] == score[-1]:
                return (x)
