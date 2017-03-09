#!/usr/bin/python3
'''
Script that uses MySQLdb to access database argv[3] and dispaly everything
matching argv[4]
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
    cur.execute("SELECT * FROM states\
    WHERE name LIKE '{}' ORDER BY id ASC".format(sys.argv[4]))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
