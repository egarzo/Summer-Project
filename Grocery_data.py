import csv



##Get The CSV file as dictionary
with open('Supermarket_data.csv') as file:
    

    reader = csv.reader(file)

    groc_dict= {}

##print the data    
    for row in reader:
        print(row)
        groc_dict[row[0]] = (row[1], row[2])

##class Cart(groc_dict):
##    
##    def __init__(self):
##        self.shopping_cart = {}
##
##    def addToCart(self, Item_Number, Price):
##            if self.shopping_cart == None:
##                self.shopping_cart[Item_Number]
##
##    def Total(self):
##            total = 0
##            for items in self:
##                    total += (self[items])*.043 + (self[items])
##            return total

            
            
    
    
##def main():
    print("Welcome to the Garzo's Market")
        
    while True:
        Item_Number = input("Enter an Item Number 1 - 40: ")

        if Item_Number in groc_dict:
            print(groc_dict[Item_Number])

        else:
            print("Item number not found")


        
        
    


