#!/usr/bin/python3
# 4-only_diff_elements.py
# Julius Okeyo <jaykopiyo@gmail.com>

def only_diff_elements(set_1, set_2):
    return (set.union((set_1 - set_2), (set_2 - set_1)))
