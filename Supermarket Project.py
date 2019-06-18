import mysql.connector

##Connection to MySQL
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host = 'localhost',
                                    database = 'Market',
                                    user = 'egarzo',
                                    password = 'Johncena5$')
    sql_select_Query = " SELECT *FROM Items"
    cursor = mySQLconnection.cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()

    #Logic Test
    path = mySQLconnection
    if path:
       print ("The Store Is Open.")
    else:
        print("There are no items in the Store. Please check connection!")


    ##Show the Items in the Store
    print("The Items In The Supermarket Are:")
    for row in records:
        print(row[0], row[1], "$",row[2])
    cursor.close()
except Error as e :
    print ("Error while connecting to MySQL", e)
finally:
    if(mySQLconnection .is_connected()):
        mySQLconnection.close()
        print("MySQL connection is closed")                                

