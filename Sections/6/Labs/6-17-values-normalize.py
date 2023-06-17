# For this program, adjust the values by dividing all values by the largest value.
# The input begins with an integer indicating the number of floating-point values that follow.

# Output each floating-point value with two digits after the decimal point, which
# can be achieved as follows:
# print('{:.2f}'.format(your_value))

# Testing in a terminal window I see
# >>> 5 // 2
# 2
# >>> your_value = 5
# >>> print('{:.2f}'.format(your_value))
# 5.00
# >>> your_value = 30.0
# >>> print('{:.2f}'.format(your_value))
# 30.00
# >>> your_value = your_value / 100.0
# >>> print('{:.2f}'.format(your_value))
# 0.30

# The 5 indicates that there are five floating-point values in the list,
# namely 30.0, 50.0, 10.0, 100.0, and 65.0. 100.0 is the largest value in the list,
# so each value is divided by 100.0