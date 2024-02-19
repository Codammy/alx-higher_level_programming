#!/usr/bin/python3
"""
 lists all states from the database hbtn_0e_0_usa
"""
import MySQLdb
import sys

user, passwd, db = sys.argv[1:]
conn = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db)
cursor = conn.cursor()
cursor.execute('select * from states order by id asc')
for row in cursor.fetchall():
    print(row)
cursor.close()
conn.close()