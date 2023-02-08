#!usr/bin/python3
# 1-my_list.py
# Julius Okeyo <jaykopiyo@gmail.com>
'''
Defines class that inherits a list and prints the list, but sorted (ascending sort)
'''
class MyList(list):
    '''
    Defines a function for printinga sorted list
    '''
    def print_sorted(self):
        print(sorted(self))
