#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    username, password, dbname = sys.argv[1:]
    conn = MySQLdb.connect(user=username, passwd=password,
                           db=dbname, host='localhost', port=3306)
    cursor = conn.cursor()
    cursor.execute('select * from states order by id asc')
    states = cursor.fetchall()
    for state in states:
        print(state)
