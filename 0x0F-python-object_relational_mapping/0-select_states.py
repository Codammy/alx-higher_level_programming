#!/usr/bin/python3
"""
script that lists all states with a name starting
with N (upper N) from the database hbtn_0e_0_usa
"""

if __name__ == '__main__':
    import MySQLdb
    import sys
    uname, passdb, dbname = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost",
                           port=3306, user=uname,
                           passwd=passdb, db=dbname,
                           charset="utf8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM states ORDER BY id")
    query_rows = cur.fetchall()
    for row in query_rows:
        print(f"{row}")
    cur.close()
    conn.close()
