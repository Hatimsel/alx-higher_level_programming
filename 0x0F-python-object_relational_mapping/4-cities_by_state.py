#!/usr/bin/python3
"""
Python script that lists all cities
from a db
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: ./script username passwd db")
    else:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             port=3306)
        cur = db.cursor()
        cur.execute("""
                    SELECT cities.id, cities.name, states.name FROM
                    cities join states on cities.state_id = states.id
                    ORDER BY cities.id ASC
                    """)
        data = cur.fetchall()

        for row in data:
            print(row)
        cursor = db.cursor()

        cursor.close()
        db.close()
