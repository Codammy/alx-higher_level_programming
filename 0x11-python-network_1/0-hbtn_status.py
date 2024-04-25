#!/usr/bin/python3
""" Script that fetches https://alx-intranet.hbtn.io/status"""


if __name__ == '__main__':
    from urllib import request
    url = 'https://alx-intranet.hbtn.io/status'
    req = request.Request(url)
    with request.urlopen(req) as res:
        data = res.read()
        custom_h = (data, type(data), data.decode())
        print('Body response:')
        print('- type: {}\n   - content: {}\n   - utf8 content: {}'
              .format(*custom_h))
