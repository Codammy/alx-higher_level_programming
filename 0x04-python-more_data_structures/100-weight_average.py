#!/usr/bin/python3
def weight_average(my_list=[]):
    t = 0
    if my_list == []:
        return t
    dic = dict(my_list)
    for k, v in dic.items():
        t += k * v
    return t / sum(dic.values())
