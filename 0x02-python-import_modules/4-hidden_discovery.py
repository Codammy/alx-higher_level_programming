#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4 as hide
    names = dir(hide)
    for name in names:
        if "__" not in name:
            print(name)
