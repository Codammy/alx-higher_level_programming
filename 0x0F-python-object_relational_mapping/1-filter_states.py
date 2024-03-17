#!/usr/bin/python3
"""
script that lists all states with a name starting with
N (upper N) from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    user, passwd, db = sys.argv[1:]
    conn = MySQLdb.connect(user=user,
                           passwd=passwd, db=db,
                           host='localhost', port=3306)
    cur = conn.cursor()
    cur.execute('select * from states where name like "N%" order by id asc')
    for state in cur.fetchall():
        print(state)
