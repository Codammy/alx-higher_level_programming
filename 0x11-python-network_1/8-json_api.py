#!/usr/bin/python3
"""
Script that takes in a letter and sends a POST
request to http://0.0.0.0:5000/search_user
with the letter as a parameter.
"""


if __name__ == '__main__':
    import requests
    import sys

    data = {'q': '' if len(sys.argv) < 2 else sys.argv[1]}
    res = requests.post('0.0.0.0:5000/search_user', data=data)
    if res.headers['Content-Type'] == 'application/json':
        js = res.json()
        if len(js):
            print(f'{[js["id"]]} {js["name"]}')
        else:
            print('No result')
    else:
        print('Not a valid JSON')
