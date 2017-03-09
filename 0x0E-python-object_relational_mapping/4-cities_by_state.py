#!/usr/bin/python3
'''
Script lists all cities in database hbtn_0e_4_usa using MySQLdb
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
    cmd = "SELECT cities.id, cities.name, states.name FROM cities\
    JOIN states ON cities.state_id = states.id ORDER BY cities.id"
    cur.execute(cmd)
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
