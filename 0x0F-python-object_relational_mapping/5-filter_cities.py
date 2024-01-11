#!/usr/bin/python3
"""
Python script that lists all cities
of the state passed as an argument from a db
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
        state = sys.argv[4]
        cur.execute("""
                    SELECT cities.name FROM cities join
                    states on cities.state_id = states.id
                    WHERE states.name = %s
                    ORDER BY cities.id ASC
                    """, (state,))
        data = cur.fetchall()

        cities = []
        for row in data:
            for col in row:
                cities.append(col)
        result = ", ".join(cities)
        print(result)
        cursor = db.cursor()

        cursor.close()
        db.close()
