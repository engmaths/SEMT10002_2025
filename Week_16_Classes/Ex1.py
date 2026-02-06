'''
Define a class to represent a shopping basket. 
The class should store the name, price, and quantity of each item in the basket. 
At initialisation, the basket should be empty, but items can be added / removed by calling appropriate functions. 
The class should also include a function for calculating the total cost of all items in the basket.

The code below describes how I would expect your Class to be used- make sure your defintions match expectations. 
In particular, add should have three arguments - the item name, the quantity, and then the cost.
'''

class ShoppingBasket:
    #Your code goes here.


#Use the following code to test your code.
basket = ShoppingBasket()
#Add two bananas, each costing £1.50.
basket.add("Banana", 2, 1.5)
#Add an apple, costing £1.
basket.add("Apple", 1, 1)
#Add three oranges, each costing £2.25
basket.add("Orange", 3, 2.25)
#Remove one banance
basket.remove("Banana", 1)

print("Total cost of basket is:", basket.total())