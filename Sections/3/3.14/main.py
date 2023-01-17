# 
# 3.14 LAB: Using math functions
# 
# Given three floating-point numbers x, y, and z, output x to the power of z, x to the power of (y to the power of z), the absolute value of (x minus y), and the square root of (x to the power of z).
# 
# Output each floating-point value with two digits after the decimal point, which can be achieved as follows:
# print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))
# 
# Ex: If the input is:
# 
# 5.0
# 1.5
# 3.2
# 
# Then the output is:
# 
# 172.47 361.66 3.50 13.13

import math
''' Type your code here. '''
x = float(input())
y = float(input())
z = float(input())

#output = x ** z, x ** (y ** z), abs(x - y), sqrt(x ** z)

your_value1 = x ** z
your_value2 = x ** (y ** z)
your_value3 = abs(x - y)
your_value4 = math.sqrt(x ** z)

print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(your_value1, your_value2, your_value3, your_value4))

# Apparently I accomplished the same thing differently
# 
# author link
# frknkrtrn
# 
# 	Ambitious
# 	643 answers
# 	1.5M people helped
# 
# Answer:
# 
# ﻿import math
# 
# x = float(input())
# 
# y = float(input())
# 
# z = float(input())
# 
# value1 = pow(x, z)
# 
# value2 = pow(x, pow(y, z))
# 
# value3 = abs(x - y)
# 
# value4 =  math.sqrt(pow(x, z))
# 
# print('{:.2f} {:.2f} {:.2f} {:.2f}'.format(value1, value2, value3, value4))

# Explanation:
# 
# *The code is in Python.
# 
# Ask the user to enter x, y, and z as floating point numbers
# 
# Calculate the each expression using math functions, pow - calculates the power, abs - calculates the absolute value, and sqrt - calculates the square root
# 
# Print the values in required format
# 
# Note that the given output is not correct. It must be:
# 
# 172.47 361.66 3.50 13.13