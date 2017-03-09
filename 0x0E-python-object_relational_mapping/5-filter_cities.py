#!/usr/bin/python3
'''
Script that lists all cities associated with a state from database
hbtn_0e_4_usa using MySQLdb
'''
if __name__ == "__main__":
    import sys
    import MySQLdb

    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cmd = "SELECT cities.name FROM states\
    JOIN cities ON states.id = cities.state_id\
    WHERE states.name=%s ORDER BY cities.id ASC"
    cur.execute(cmd, (sys.argv[4],))
    list = []
    for row in cur.fetchall():
        list.append(row[0])
    print(', '.join(list))
    cur.close()
    db.close()
