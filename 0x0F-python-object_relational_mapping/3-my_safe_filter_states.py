#!/usr/bin/python3
"""
write a script that takes in arguments and displays all
values in the states table of hbtn_0e_0_usa
where name matches the argument. But this time,
write one that is safe from MySQL injections!
Your script should take 4 arguments:
mysql username, mysql password, database name and state name searched
save from sql injections
You must use format to create the SQL query with the user input
Results must be sorted in ascending order by states.id
"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    q = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    cur.execute(q, (sys.argv[4],))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()
