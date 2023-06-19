#!/usr/bin/python3
# a script that lists all states with a name starting with N
# (upper N) from the database hbtn_0e_0_usa
import MySQLdb
import sys

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306,
                         user=sys.argv[1], password=sys.argv[2],
                         database=sys.argv[3])
    c = db.cursor()
    c.execute(
        """SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER
        BY states.id""")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
