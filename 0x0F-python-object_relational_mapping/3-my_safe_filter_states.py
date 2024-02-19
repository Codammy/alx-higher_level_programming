#!/usr/bin/python3
"""displays all values in the states table of hbtn_0e_0_usa
where name matches the argument
"""


if __name__ == "__main__":
    import MySQLdb
    from sys import argv
    user, passwd, db, match_ = argv[1:]
    Engine = MySQLdb.connect(host="localhost", port=3306, user=user,
                             passwd=passwd, db=db)
    cursor = Engine.cursor()
    cursor.execute('select * from states where name="{}" \
            order by id asc'.format(match_))
    for row in cursor.fetchall():
        if row[1][0] == match_
        print(row)
    cursor.close()
    Engine.close()
