#!/usr/bin/python3
"""Lists record with on @hbtn_0e_4_usa DB"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost', user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    cur.execute("SELECT cities.id, cities.name,"
                + " states.name FROM cities LEFT JOIN"
                + " states ON states.id=cities.state_id")
    rows = (cur.fetchall())
    for row in rows:
        print(row)
