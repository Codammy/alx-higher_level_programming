#!/usr/bin/python3
""" text indentation """


def text_indentation(text):
    """prints a text with 2 new lines after . ? and : """
    if type(text) is not str:
        raise TypeError("text must be a string")
    ln = len(text)
    i = 0
    while i < ln:
        c = text[i]
        print(c, end="")
        i += 1
        if c == '.' or c == '?' or c == ':':
            print('\n')
            try:
                if text[i] == ' ':
                    i += 1
            finally:
                continue
