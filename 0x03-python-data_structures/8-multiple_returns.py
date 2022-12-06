#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        y = None
        u = len(sentence)
    else:
        y = sentence[0]
        u = len(sentence)
    return((u, y))
