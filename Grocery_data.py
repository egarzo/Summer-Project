import csv



##Get The CSV file as dictionary
with open('Supermarket_data.csv') as file:
    

    reader = csv.reader(file)

    groc_dict= {}

##print the data
    print("Welcome to the Garzo's Market")
    for row in reader:
        print(row)
        groc_dict[row[0]] = [row[2]]


    def addToCart(groc_dict):
        
        shopping_cart = []
        
        for Item_number in groc_dict:
            if shopping_cart == None:
                shopping_cart.append(Item_Number)

            print("added to cart")
            
            print(shopping_cart)

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
        
    else:
        print("Item number not found, Please enter a valid Item Number!")
        
    
    add = input("Would you like add more items to cart? Yes or No?: ")
    if add == "Yes":
        addToCart(Item_Number)

    else:
        break
        


    

            


        
        
    


