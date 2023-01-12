#!/usr/bin/python3
# 10-best_score.py
# Julius Okeyo <jaykopiyo@gmail.com>

def best_score(a_dictionary):
    highest = 0
    for key in a_dictionary.keys():
        if a_dictionary[key] > highest:
            highest = a_dictionary[key]
    return (highest)
