#!/usr/bin/python3
"""
script that takes in the name of a state as
an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    usr, key, dbname, state = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost",
                           db=dbname,
                           user=usr,
                           passwd=key,
                           port=3306)
    cursor = conn.cursor()
    cursor.execute("SELECT cities.name FROM cities\
            JOIN states ON cities.state_id = states.id\
            WHERE states.name=%s ORDER BY cities.id ASC", (state, ))
    data = cursor.fetchall()
    dl = len(data)
    for d in data:
        print(d[0], end=", " if 1 < dl else "\n")
        dl -= 1
