#!/usr/bin/python3
"""
Script that takes in a URL and an email, sends a POST request
to the passed URL with the email as a parameter, and displays the
body of the response (decoded in utf-8)
"""


if __name__ == '__main__':
    from urllib import request, parse
    import sys

    params = {'email': sys.argv[2]}
    params = parse.urlencode(params).encode('ascii')
    req = request.Request(sys.argv[1])
    with request.urlopen(req) as res:
        data = res.read()
        print(data.decode('utf-8'))
