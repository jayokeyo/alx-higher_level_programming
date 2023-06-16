#!/usr/bin/python3
'''
lists all states from the database hbtn_0e_0_usa
'''
import MySQLdb
import sys

if __name__ == __"__main__":
    db = MqSQLdb.connect(
            host="localhost", 
            port=3306, 
            user=sys.argv[1], 
            passwd=sys.argv[2], 
            db=sys.argv[3]
            )
    cursor = db.cursor()
    query = "SELECT states FROM hbtn_0e_0_usa ORDER BY states ASC"
    cursor.execute(query)
    [print(state) for state in cursor.fetchall()]
