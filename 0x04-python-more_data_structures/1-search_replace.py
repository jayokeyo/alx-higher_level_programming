#!/usr/bin/python3
# 1-search_replace.py
# Julius Okeyo <jaykopiyo@gmail.com>

def search_replace(my_list, search, replace):
    return (list(map(lambda x: x = replace if x == search else x = my_list[i] for i in range(len(my_list)), my_list)))
