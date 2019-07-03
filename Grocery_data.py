import csv



##Get The CSV file as dictionary
with open('Supermarket_data.csv') as file:
    

    reader = csv.reader(file)

    groc_dict= {}

##print the data
    print("Welcome to the Garzo's Market")
    for row in reader:
        print(row)
        groc_dict[row[0]] = (row[1], row[2])

        
        shopping_cart = {}

        def addToCart(Item_Number):
            if shopping_cart == None:
                shopping_cart.update[Item_Number]
                
                print ("Added to cart")


                print (shopping_cart)

##        def Subtotal():
##        
##
##        def Total():
##            
##
##        def returnCart():
##            return.....
##            
##    
    
######Unit Testing

    while True:
        
        Item_Number = input("Enter an Item Number 1 - 40: ")
    

        if Item_Number in groc_dict:
            print(groc_dict[Item_Number])
            
            addToCart(Item_Number)

        else:
            print("Item number not found, Please enter a valid Item Number!")

    

            


        
        
    


