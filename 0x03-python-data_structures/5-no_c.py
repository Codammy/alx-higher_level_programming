#!/usr/bin/python3

def no_c(my_string):
    news = ""
    for i in my_string:
        if 'c' in i or 'C' in i:
            continue
        news += i
    return news
