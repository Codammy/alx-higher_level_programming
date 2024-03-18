#!/usr/bin/python3
"""
script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    name, key, db, searched = sys.argv[1:]
    conn = MySQLdb.connect(host='localhost',
                           port=3306,
                           user=name,
                           passwd=key,
                           db=db)
    cur = conn.cursor()
    cur.execute('select * from states where name="{}" order \
                 by id asc'.format(searched))
    for state in cur.fetchall():
        if state[1] == searched:
            print(state)
