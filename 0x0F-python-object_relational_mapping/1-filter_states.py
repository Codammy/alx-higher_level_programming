#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""
if __name__ == "__main__":
    import MySQLdb
    import sys
    user, key, db = sys.argv[1:]
    con = MySQLdb.connect(user=user,
                          passwd=key, db=db,
                          host="localhost", port=3306)
    current = con.cursor()
    current.execute("SELECT * FROM states WHERE name \
            LIKE 'N%' ORDER BY id ASC")
    values = current.fetchall()
    for v in values:
        if v[0][1] == 'N':
            print(v)
