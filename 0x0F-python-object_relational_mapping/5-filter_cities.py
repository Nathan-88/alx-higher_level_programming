#!/usr/bin/python3
"""
a script that takes in the name of a state as an argument and
lists all cities of that state, using the database hbtn_0e_4_usa
Results must be sorted in ascending order by cities.id
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
        "SELECT c.name FROM `cities` c JOIN `states` s ON c.state_id = s.id WHERE s.name = '{}' ORDER BY c.id".format(sys.argv[4]))
    result = c.fetchall()
    for rows in range(len(result)):
        print(result[rows][0], end="")
        if rows < len(result) - 1:
            print(", ", end="")
    print()
