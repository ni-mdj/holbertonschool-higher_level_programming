#!/usr/bin/python3
"""Script that displays all values in the states table where name matches the argument"""

import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    query = "SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4])
    cur.execute(query)
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()