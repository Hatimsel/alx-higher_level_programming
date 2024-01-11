#!/usr/bin/python3
"""
Python script that lists all states
with a name matches the argument from a db
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if (len(sys.argv) < 2):
        print("Usage: ./script username passwd db state's name")
    else:
        db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                             passwd=sys.argv[2], db=sys.argv[3],
                             port=3306)
        cur = db.cursor()
        argument = sys.argv[4]
        cur.execute("""
                    SELECT * FROM states WHERE states.name LIKE %s
                    ORDER BY states.id ASC
                    """, (argument,))
        data = cur.fetchall()

        for row in data:
            print(row)
        cursor = db.cursor()

        cursor.close()
        db.close()
