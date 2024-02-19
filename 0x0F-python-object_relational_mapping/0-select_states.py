#!/usr/bin/python3
import MySQLdb
import sys
user, passwd, db = sys.argv[1:]
Engine = MySQLdb.connect(host="localhost", port=3306, user=user,
                         passwd=passwd, db=db)
cursor = Engine.cursor()
cursor.execute('select * from states order by id asc')
for row in cursor.fetchall():
    print(row)
cursor.close()
Engine.close()
