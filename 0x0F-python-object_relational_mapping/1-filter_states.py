#!/usr/bin/python3
"""
Python script that lists all states
with a name starting with N from a db
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: user passwd db")
    else:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             port=3306)
        cur = db.cursor()
        cur.execute("""
        SELECT * FROM states WHERE states.name
        LIKE 'N%' ORDER BY states.id ASC
        """)
        data = cur.fetchall()

        for row in data:
            print(row)
