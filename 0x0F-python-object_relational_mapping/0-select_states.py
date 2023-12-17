#!/usr/bin/python3
"""
return table values
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    myDatabase = mySQLdb.connect(host="localhost", user=sys.argv[1],
                                passwd=sys.argv[2], db=sys.argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute("SELECT * FROM states")
    for row in cursor.fetchall():
        print(row)
    cursor.close()
    db.close()
