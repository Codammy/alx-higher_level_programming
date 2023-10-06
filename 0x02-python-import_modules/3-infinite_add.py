#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sumUp = 0
    argLen = len(sys.argv)
    for i in range(1, argLen):
        num = int(sys.argv[i])
        sumUp += num
    print("{}".format(sumUp))
