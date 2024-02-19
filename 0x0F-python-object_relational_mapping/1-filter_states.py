#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user, passwd, db = argv[1:]
    Engine = MySQLdb.connect(host="localhost", port=3306, user=user,
                             passwd=passwd, db=db)
    cursor = Engine.cursor()
    cursor.execute('select * from states where name like "N%" order by id asc')
    for row in cursor.fetchall():
        if row[1][0] == 'N':
            print(row)
    cursor.close()
    Engine.close()
