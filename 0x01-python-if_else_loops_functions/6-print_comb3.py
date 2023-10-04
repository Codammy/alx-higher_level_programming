#!/usr/bin/python3
for i in range(48, 58):
    for j in range(i + 1, 58):
        print("{}{}".format(chr(i), chr(j)), end="")
        if (i < 56):
            print(end=", ")
print()
