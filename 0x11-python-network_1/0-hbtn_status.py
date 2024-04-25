#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as res:
        data = res.read()
        print('Body response:')
        print(f'\t- type: {type(data)}\n\t\
- content: {data}\n\t\
- utf8 content: {str(data.decode())}')
