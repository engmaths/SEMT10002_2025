'''
Stack-based algorithms are used throughout computer science- one area where they are used is in *parsing* your code before it is executed. 
Parsing means checking your code for syntax errors before it is run.

 In Python (and most other programming languages), we make extensive use of brackets- 
 curly brackets () to call a function or define a tuple, square brackets [] to make a list, or braces {} to make a dict. 
 For our code to be valid syntax, all parentheses must be balanced- in other words, every ```(``` must match with a corresponding ```)```. 
 If not, the code is invalid. For example:

x = (1, 2, 3) #This is valid Python code
x = (1, 2	  #This is invalid Python code
x = ([1, 2], 3) #This is also valid Python code
x = ([1, 2], []) #This is valid Python code
x = ([1, 2], ]) # This is invalid Python code

Before your code is executed, the Python interpreter will check to see whether your code only contains balanced parantheses. 
It'll do this, by using a stack. The basic idea is to go through the string, a character as a time. 
Each time we come across an opening bracket, we add it to our stack. 
Each time we come across a closing bracket, we pop the top item off of our stack and check to see if it matches the closing bracket. 
If it doesn't, then we have unbalanced parantheses. 
If we go through the entire string, without finding any mismatched parentheses, *and* the stack is empty, then our string has balanced parantheses. 

Implement an algorithm for checking whether a string contains only balanced parentheses. 
Your function should take a string as input and return either False (if it's not balanced) or True (if it's balanced).
'''

def is_balanced(string):
    #Your code goes here
	return True

def test_is_balanced():

    assert is_balanced("(){}[]") == True, "Test case 1 failed"
    assert is_balanced("({[]})") == True, "Test case 2 failed"
    assert is_balanced("({[})") == False, "Test case 3 failed"
    assert is_balanced("({[}") == False, "Test case 4 failed"
    assert is_balanced("") == True, "Test case 5 failed"
    assert is_balanced("({[hello]})") == True, "Test case 6 failed"
    assert is_balanced("[x**2 for x in range(10)]") == True, "Test case 7 failed"
    assert is_balanced("for i in range(10):\n\tprint(i)") == True, "Test case 8 failed"
    print("All test cases passed")

test_is_balanced()