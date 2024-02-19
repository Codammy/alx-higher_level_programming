#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    # user, passwd, db = argv[1:]
    Engine = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cursor = Engine.cursor()
    cursor.execute('select * from states order by id asc')
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    Engine.close()
