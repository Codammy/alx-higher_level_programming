#!/usr/bin/python3
"""
    script that takes in an argument
    and displays all values in the states table
    of hbtn_0e_0_usa where name matches the argument.
"""


if __name__ == "__main__":
    import sys
    import MySQLdb

    usr, key, dbname, to_match = sys.argv[1:]
    conn = MySQLdb.connect(host="localhost",
                           passwd=key,
                           db=dbname,
                           port=3306,
                           user=usr)
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM states WHERE\
            name=%s """ (to_match, ))
    values = cursor.fetchall()
    for v in values:
        if v[1] == to_match:
            print(v)
