#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for elements in row:
            print('{:d}'.format(elements), end ='\n' if elements == row[-1] else ' ')