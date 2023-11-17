#!/usr/bin/python3
"""
Script that lists all cities
from the database hbtn_0e_4_usa
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Script should take 3 arguments")
    else:
        db = MySQLdb.connect(
            host='localhost', port=3306,
            user=sys.argv[1], passwd=sys.argv[2],
            db=sys.argv[3]
        )
        cursor = db.cursor()
        cursor.execute("SELECT c.id, c.name, s.name FROM cities c\
                       JOIN states s ON s.id = c.state_id\
                       ORDER BY c.id ASC"
                       )
        result = cursor.fetchall()
        for row in result:
            print(row)
