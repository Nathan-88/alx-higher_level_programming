#!/usr/bin/python3
"""
a script that lists all states with a name starting with N
(upper N) from the database hbtn_0e_0_usa:
Your script should take 3 arguments:
mysql username, mysql password and database name
Results must be sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM `states` WHERE name LIKE 'N%' ORDER BY states.id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
