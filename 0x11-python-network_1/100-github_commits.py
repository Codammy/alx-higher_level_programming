#!/usr/bin/python3
"""
 Python script that takes 2 arguments in order to solve this challenge.
"""


if __name__ == '__main__':
    import sys
    import requests

    owner, repo = sys.argv[1:]
    r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits',
                     params={"per_page": 10}
                     )
    # if r.ok:
    json_data = r.json()
    for data in json_data:
        sha = data['sha']
        commit = data['commit']
        print('{}: {}'.format(sha, commit['author']['name']))
