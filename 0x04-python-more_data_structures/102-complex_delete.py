#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    todel = list()
    for k, v in a_dictionary.items():
        if value == v:
            todel.append(k)
    for i in todel:
        del a_dictionary[i]
    return a_dictionary
