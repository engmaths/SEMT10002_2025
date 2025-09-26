#Binary to decimal conversion. Replace the '???' with your code.
binary_string = '1011'
decimal_value = ((int(binary_string[0]) * 2**3) +
(int(binary_string[1])* 2**2) + 
(int(binary_string[2])* 2**1) + 
(int(binary_string[3])* 2**0))

print(decimal_value)

#Decimal to binary conversion. Replace the '???' with your code.
decimal_value2 = 13 
binary_string = str(decimal_value2 // (2**3)) + str((decimal_value2) // (2**2)) + str((decimal_value2-12) // (2**1)) + str((decimal_value2-14) // (2**0))
print(binary_string)