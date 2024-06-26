#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as res:
        data = res.read()
        custom_h = (type(data), data, data.decode())
        print('Body response:')
        print('\t- type: {}\n\t- content: {}\n\t- utf8 content: {}'
              .format(*custom_h))
