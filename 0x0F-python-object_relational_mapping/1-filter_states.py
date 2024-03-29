#!/usr/bin/python3
'''
lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(
            user = sys.argv[1], 
            passwd = sys.argv[2], 
            db = sys.argv[3]
            )
    cursor = db.cursor()
    query = "SELECT * FROM `states` ORDER BY 'id'"
    cursor.execute(query)
    [print(state) for state in cursor.fetchall() if state[1][0] == "N"]
