#!/usr/bin/python3

def no_c(my_string):

    '''This function removes every occurance of c 
both capital and small letters'''
    
    new_string = ''
    for char in my_string:
        if char != 'c' and char != 'C':
            new_string += char
    return new_string
