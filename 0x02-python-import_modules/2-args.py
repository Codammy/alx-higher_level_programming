#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argNum = len(sys.argv)
    print("{}".format(argNum - 1), end=" ")
    if argNum == 2:
        print("argument:")
    elif argNum == 1:
        print("arguments.")
    else:
        print("arguments:")
    for i in range(1, argNum):
        print("{}: {}".format(i, sys.argv[i]))
