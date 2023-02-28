# Print "user_num1 is negative." if user_num1 is less than 0. End with newline.
# Assign user_num2 with 4 if user_num2 is greater than 8. Otherwise, print "user_num2 is less than or equal to 8.". End with newline.

user_num1 = int(input())
user_num2 = int(input())

if user_num1 < 0:
	print('user_num1 is negative.')

if user_num2 > 8:
	user_num2 = 4
else:
	print('user_num2 is less than or equal to 8.')

print('user_num2 is', user_num2)
