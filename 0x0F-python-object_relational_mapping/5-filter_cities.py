#!/usr/bin/python3
"""
Script that takes in an argument and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument.
"""
import MySQLdb
import sys


if __name__ == "__main__":
    if len(sys.argv) < 4:
        print("Script should take 3 arguments")
    else:
        db = MySQLdb.connect(host='localhost', port=3306,
                             user=sys.argv[1], passwd=sys.argv[2],
                             db=sys.argv[3])
        cursor = db.cursor()
        query = "SELECT c.name FROM cities c\
                JOIN states s ON c.state_id = s.id\
                WHERE s.name LIKE %s\
                ORDER BY c.id ASC"
        state = sys.argv[4]
        cursor.execute(query, (state,))
        result = cursor.fetchall()
        for row in result:
            for col in row:
                print(col + ", ", end='')
        cursor.close()
        db.close()
