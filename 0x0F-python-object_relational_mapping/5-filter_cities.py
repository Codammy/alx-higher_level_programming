#!/usr/bin/python3
"""
script that takes in the name of a state
as an argument and lists all cities of that state,
using the database hbtn_0e_4_usa
"""


if __name__ == '__main__':
    import MySQLdb
    import sys

    user, passwd, db, state = sys.argv[1:]
    conn = MySQLdb.connect(user=user, passwd=passwd, db=db,
                           host='localhost', port=3306)
    cur = conn.cursor()
    cur.execute('select cities.name from cities,\
                 states where cities.state_id=states.id\
                 and states.name=%s', (state, ))
    cities = cur.fetchall()
    to_print = len(cities)
    for city in cities:
        print(city[0], end=f'{", " if to_print > 1 else ""}')
        to_print -= 1
    print()
