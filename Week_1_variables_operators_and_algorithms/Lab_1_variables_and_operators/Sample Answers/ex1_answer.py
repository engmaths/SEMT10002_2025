'''
## Exercise 1 - Binary to Decimal Conversion

We saw in the lecture notes that computers represent integers using a binary code.
We can convert from binary to decimals to remembering that each digit corresponds to a particular power of 2, 
and then summing up the values of each digit. In this exercise, you should write some code to:

1. Converting a binary "string" to a decimal number (Recall that, for example, `my_string[3]` will access the 4th character of the string variable)
2. Converting a decimal number into a binary string (You may want to use the modulo operator - `%` - to do this).

Start by writing code that solves only the examples given.  
Given time, try writing code that works for different input values.  
You can assume the same sizes as given.
'''

#Binary to decimal conversion. Replace the '???' with your code.
binary_string = '1101'

#First, we need to take take each element of the string and convert it to an integer using int() 
#Next we need multiply the value of each element by the amount it represents- 
# i.e the first number is multiplied by 8 (=2^3), the next by 4 (=2^2) and so on.
decimal_value = ((int(binary_string[0]) * 2**3) +
(int(binary_string[1])* 2**2) + 
(int(binary_string[2])* 2**1) + 
(int(binary_string[3])* 2**0))

print(decimal_value)

#Decimal to binary conversion. Replace the '???' with your code.
decimal_value2 = 13
#To find the first bit of our binary number we divide by 8. 
#If the result is bigger than 1, the first bit should be 1. 
#If its less than 1, the first bit should be 0.
#We can achieve this using floor division (//) which will round the result down to the nearest integer.
#To find the next bit, we first find the remainder when the decimal value is divided by 8 (with the modulo operator, %)
#We then use floor division (// 4) to determine whether the bit should be a 1 or a 0. 
#Repeating this pattern for each digit, we get our binary number.
binary_string = (str(decimal_value2 // (2**3)) + 
str(((decimal_value2) % (2**3)) // 2**2) + 
str(((decimal_value2) % (2**2)) // 2**1) + 
str(((decimal_value2) % (2**1)) // 2**0))
print(binary_string)
