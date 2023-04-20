#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument
and lists all cities of that state,
using the database hbtn_0e_4_usa
Your script should take 4 arguments:
mysql username, mysql password, database name and
state name (SQL injection free)

"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cur = db.cursor()
    cur.execute("SELECT c.name FROM `cities` c JOIN states s ON\
                s.id = c.state_id WHERE s.name = '{}' ORDER\
                BY c.id".format(sys.argv[4]))
    rows = cur.fetchall()
    if len(rows) < 1:
        print("")
    else:
        for row in range(len(rows)):
            print("{}".format(rows[row][0]), end="")
            if row < len(rows)-1:
                print(", ", end="")
        print("")
    cur.close()
    db.close()
