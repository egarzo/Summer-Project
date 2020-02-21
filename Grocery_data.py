import csv



##Get The CSV file as dictionary
with open('Supermarket_data.csv') as file:
    

    reader = csv.reader(file)

    groc_dict= {}
    shopping_cart = []

##print the data
    print("Welcome to the Garzo's Market")
    for row in reader:
        print(row)
        groc_dict[row[0]] = [row[1],row[2]]


    def addToCart(groc_dict):
        
        for Item_number in groc_dict:
            shopping_cart.append(Item_Number)
            

            
            #print(groc_dict, "added to cart") 

            print (shopping_cart)
            
            
        return shopping_cart
        

##    def Subtotal(shopping_cart):
##        subtotal = 0
##        for Item_Number in shopping_cart:
##            subtotal += Item_Number
##            print ("The Subtotal is:")
##            print (subtotal)
##        return subtotal
        

##    def Total():
            

    def returnCart(shopping_cart):
        print (shopping_cart)
            
    
    
######Unit Testing

while True:
        
    Item_Number = input("Enter an Item Number 1 - 40: ")
    if Item_Number in groc_dict:
        addToCart(Item_Number)
        print(groc_dict[Item_Number])
        
    else:
        print("Item number not found, Please enter a valid Item Number!")
        
    
    add = input("Would you like add more items? Yes or No?: ")
    if add == "Yes":
        addToCart(groc_dict[Item_Number])

    else:
        
        addToCart(groc_dict[Item_Number])
        returnCart(shopping_cart)
    

        break
#print("Items Scanned: ")




            

