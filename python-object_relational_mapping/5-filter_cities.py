#!/usr/bin/python3
"""Lists record from argv in @hbtn_0e_4_usa DB"""
import MySQLdb
from sys import argv


if __name__ == "__main__":
    db = MySQLdb.connect(
            host='localhost', user=argv[1], passwd=argv[2], db=argv[3])

    cur = db.cursor()

    unpack = 0
    cnt = 0

    try:
        cur.execute("SELECT cities.name FROM cities" +
                    " LEFT JOIN states ON " +
                    "cities.state_id=states.id WHERE " +
                    "states.name=%s", (argv[4], ))

        rows = (cur.fetchall())

        for row in rows:
            if unpack:
                unpack = unpack + row
            else:
                unpack = row

        for item in unpack:
            if cnt != 0 and item is not None:
                print(", ", end="")

            print(f"{item}", end="")
            cnt = cnt + 1

        print()

    except TypeError:
        print()
        quit()
