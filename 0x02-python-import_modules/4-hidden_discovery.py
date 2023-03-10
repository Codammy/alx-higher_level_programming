#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    cont = dir(hidden_4)
    for i in cont:
        if i[:2] == '__':
            continue
        print("{}".format(i))
