#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list):
        num_ = 0
        denom_ = 0
        for tup in my_list:
            num += (tup[0] * tup[1])
            denom += (tup[1])
        return (num/denom)
