#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user, passwd, db = argv[1:]
    conn = MySQLdb.connect(host="localhost", port=3306, user=user, db=db, passwd=passwd)
    cur = conn.cursor()
    cur.execute("select * from cities natural join states")
    for data in cur.fetchall():
        print(data)

