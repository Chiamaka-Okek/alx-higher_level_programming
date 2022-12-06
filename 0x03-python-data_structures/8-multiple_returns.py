#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence == "":
        sentence[0] = None
    else:
        y = sentence[0]
        u = len(sentence)
        return((u, y))
