'''
The code stub below partially defines a class for a binary search tree. 
We've provided you with an initialisation method, and an insert method. 
However, the search method hasn't been implemented. 
This method should check whether a value is in the tree, returning ```True``` if it is and ```False``` if it isn't. 
A good way to approach this is by using recursion- if the value of the current node matches the value you are searching for, then you return ```True```.
If not, then you need to look at either the left or right child- If the value you are looking for is less than the current node, 
you would check the left child. If the left child doesn't exist, then return ```False```. 
If it does, then you should return whatever result you get from calling the search method on the left-hand tree.

Implement the search method for a Binary Search Tree. 
You can use the test function test_search to check whether your code is correct. 
'''

class BinarySearchTree:

	def __init__(self, value):
		self.value = value
		self.left = None
		self.right = None

	def insert(self, value):

		if value < self.value:
			if self.left is None:
				self.left = BinarySearchTree(value)
			else:
				self.left.insert(value)
		elif value > self.value:
			if self.right is None:
				self.right = BinarySearchTree(value)
			else:
				self.right.insert(value)
		else:
			print("Error- value is also in Tree")

	def search(self, value):

        #Your code goes here
        
		return False

	def pretty_print(self, indent=0):
	    if self.right:
	        self.right.pretty_print(indent + 4)
	    print(" " * indent + str(self.value))
	    if self.left:
	        self.left.pretty_print(indent + 4)

def test_search():

	#Values to store in the binary search tree
	values_to_add = [5, 8, 2, 4, 6, 7, 3]

	#Create a root node with the first element of the list
	root = BinarySearchTree(values_to_add[0])

	#Add remaining elements to the tree
	for val in values_to_add[1:]:
		root.insert(val)

	print("Running tests")
	assert root.search(5)==True, "Test 1"
	assert root.search(8)==True, "Test 2"
	assert root.search(2)==True, "Test 3"
	assert root.search(4)==True, "Test 4"
	assert root.search(6)==True, "Test 5"
	assert root.search(7)==True, "Test 6"
	assert root.search(3)==True, "Test 7"
	assert root.search(10)==False , "Test 8"
	print("Tests finished")

test_search()