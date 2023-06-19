#!/usr/bin/python3
"""
a script that lists all cities from the database hbtn_0e_4_usa
Your script should take 3 arguments: mysql username, mysql
password and database name
You must use the module MySQLdb (import MySQLdb)
Your script should connect to a MySQL server running on localhost at port 3306
Results must be sorted in ascending order by cities.id
You can use only execute() once
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
    c.execute(
        "SELECT c.id, c.name, s.name FROM `cities` c JOIN\
        `states` s ON c.state_id = s.id ORDER BY id")
    result = c.fetchall()
    for rows in result:
        print(rows)
