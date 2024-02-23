#!/usr/bin/python3
"""
takes in the name of a state as an argument and lists all cities of that state, using the database hbtn_0e_4_usa
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv

    usr, passwd, db, state = argv[1:]
    conn = MySQLdb.connect(user=usr, passwd=passwd, db=db)
    cur = conn.cursor()
    # cur.execute('select cities.name from cities, states where states.name=%s and states.id=cities.state_id', (state, ))
    """ or """
    try:
        cur.execute('select cities.name from cities join states on states.id=cities.state_id and states.name=%s', (state, ))                                      
        cities_in_state = cur.fetchall()
        len = len(cities_in_state) - 1
        for city in cities_in_state:
            print(city[0], end=('' if city[0] == cities_in_state[len][0] else ', '))
    except Exception:
        pass
    print()
