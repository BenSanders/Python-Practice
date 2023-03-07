#while expression:  # Loop expression
	# Loop body: Sub-statements to execute
	# if the loop expression evaluates to True

# Statements to execute after the expression evaluates to False

curr_power = 2
user_char = 'y'

while user_char == 'y':
	print(curr_power)
	curr_power = curr_power * 2
	user_char = input()

print('Done')