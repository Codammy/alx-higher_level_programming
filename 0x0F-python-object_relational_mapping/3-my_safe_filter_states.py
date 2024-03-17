#!/usr/bin/python3
"""Preventing sql injection"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    nm, key, db, srch = sys.argv[1:]
    conn = MySQLdb.connect(user=nm, passwd=key,
                           db=db, host='localhost',
                           port=3306)
    cur = conn.cursor()
    cur.execute('select * from states where name=%s order by id asc', (srch, ))
    for state in cur.fetchall():
        if (state[1] == srch):
            print(state)
