#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments:
mysql username, mysql password and database name
you can use only execute() once
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name FROM `cities` c JOIN states s ON\
                 s.id = c.state_id ORDER BY c.id")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
