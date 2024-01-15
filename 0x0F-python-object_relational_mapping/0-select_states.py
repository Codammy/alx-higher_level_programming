#!/usr/bin/python3
"""
"""

if __name__ == '__main__':
    import MySQLdb, sys
    uname, passwd, dbname = sys.argv[1:]
    conn = MySQLdb.connect(host: "localhost", port: 3306, user: uname, passwd: passwd, charset="utf-8")
    cur = conn.cursor()
    cur.execute("SELECT * FROM state ORDER BY id")
    query_rows = cur.fetchall()
    i = 0;
    for row in query_rows:
        print(f"({i}, {row})")
        i++
    cur.close()
    conn.close()
