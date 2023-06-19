#!/usr/bin/python3
"""
a script that takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument
But this time, write one that is safe from MySQL injections!
Your script should take 4 arguments: mysql username, mysql
password, database name and state name searched (safe from MySQL injection)
You must use the module MySQLdb (import MySQLdb)
Results must be sorted in ascending order by states.id
"""
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3]
    )

    c = db.cursor()

    query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"
    c.execute(query, (sys.argv[4],))

    result = c.fetchall()
    for row in result:
        print(row)

    c.close()
    db.close()
