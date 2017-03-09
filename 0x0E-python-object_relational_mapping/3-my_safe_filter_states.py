#!/usr/bin/python3
'''
Script that uses MySQLdb to access database argv[3] and print out everything
that is the same as argv[4]. ALSO protects against SQL injection
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
    cmd = "SELECT * FROM states WHERE name=%s ORDER BY id ASC"
    cur.execute(cmd, (sys.argv[4],))
    for row in cur.fetchall():
        print(row)
    cur.close()
    db.close()
