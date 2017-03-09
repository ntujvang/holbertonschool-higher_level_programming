#!/usr/bin/python3
'''
Script uses MySQLdb to access database argv[3] and prints out anything
starting with "N"
'''
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost",
                         user=sys.argv[1],
                         password=sys.argv[2],
                         database=sys.argv[3],
                         port=3306)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
