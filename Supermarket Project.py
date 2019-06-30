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
        
        
        item_number = row[0]
        
        item_name = row[1]
        
        price = row[2]
##Calculate Cost        

    class Cart(records):
        
        def __init__(self, item_number, item_name, price):
            self.item_number = item_number
            
            self.item_name = item_name
            
            self.price = price

        def __str__(self):
       
            print( "%s, %s, %s" %(self.item_number, self.item_name, self.price))

        def addItems(self, item_number, item_name, price):
            self.update({item_number:price})

        def Total_Cost(self):
            total_cost = 0
            for item_number in self:
                total_cost += (self[item_number])
                return total

            
        def Items_p(self):
            return self


    cursor.close()

except Error as e :

    print ("Error while connecting to MySQL", e)
    

#finally:

    #if(mySQLconnection .is_connected()):

        #mySQLconnection.close()

        #print("MySQL connection is closed")                                


##    class CursorByName():
##        def __init__(self,cursor):
##            self._cursor = cursor
##
##        def __iter__(self):
##            return self
##
##        def __next__(self):
##            row = self._cursor.__next__()
##
##            return { description[0]: row[col] for col, description in enumerate(self._cursor.description)}
##
##        for row in CursorByName(cur):
##            print(row)

        


