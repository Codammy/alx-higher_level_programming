#!/usr/bin/python3
def weight_average(my_list=[]):
    sum = 0
    if my_list == []:
        return sum
    for tup in my_list:
        i, j = tup
        sum += i * j / j
    return sum
