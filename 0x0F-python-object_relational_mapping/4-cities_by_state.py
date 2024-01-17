#!/usr/bin/python3
"""
Write a script that lists all cities
from the database hbtn_0e_4_usa
"""
if __name__ == "__main__":
    import sys
    import MySQLdb

    usr, key, dbname = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost", passwd=key,
                           db=dbname, port=3306,
                           user=usr)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM cities ORDER BY id ASC")
    values = cursor.fetchall()
    for v in values:
        print(v)
