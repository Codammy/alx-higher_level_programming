#!/usr/bin/python3
"""
Script that takes in a URL, sends a request to the URL
and displays the value of the variable X-Request-Id
in the response header
"""


if __name__ == '__main__':
    import requests
    import sys

    res = requests.get(sys.argv[1])
    try:
        hvalue = res.headers['X-Request-Id']
        print(hvalue)
    except KeyError as e:
        pass
