#!/usr/bin/python3
"""
Python script that takes your GitHub credentials (username and password)
and uses the GitHub API to display your id
"""


if __name__ == '__main__':
    import requests
    import sys

    user, key = sys.argv[1:]
    auth = {"user": user, "password": key}
    res = requests.get(f'https://api.github.com/users/{user}',
                       auth=(user, key))
    json_data = res.json()
    if res.ok:
        print(json_data['id'])
    else:
        print(None)
