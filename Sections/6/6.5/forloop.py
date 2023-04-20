# for variable in container:
# 	# Loop body: Sub-statements to execute
# 	# for each item in the container
# 
# # Statements to execute after the for loop is complete

# for name in ['Bill', 'Nicole', 'John']:
#   print('Hi {}!'.format(name))
# The first iteration assigns the variable name with 'Bill' and prints 'Hi Bill!' to the screen.
# The second iteration assigns the variable name with 'Nicole' and prints 'Hi Nicole!'.
# The third iteration assigns the variable name with 'John' and prints 'Hi John!'.

# Dictionaries and for loops
# channels = {
# 	'MTV': 35,
# 	'CNN': 28,
# 	'FOX': 11,
# 	'NBC': 4,
# 	'CBS': 12
# }
# 
# for c in channels:
# 	print('{} is on channel {}'.format(c, channels[c]))

# Using a for loop to access each character of a string
# my_str = ''
# for character in "Take me to the moon.":
# 	my_str += character + '_'
# print(my_str)

# Shop Revenue
# daily_revenues = [
# 	2356.23,  # Monday
# 	1800.12,  # Tuesday
# 	1792.50,  # Wednesday
# 	2058.10,  # Thursday
# 	1988.00,  # Friday
# 	2002.99,  # Saturday
# 	1890.75   # Sunday
# ]
# 
# total = 0
# for day in daily_revenues:
# 	total += day
# 
# average = total / len(daily_revenues)
# 
# print('Weekly revenue: ${:.2f}'.format(total))
# print('Daily average revenue: ${:.2f}'.format(average))

# Reversed names
# names = [
# 	'Biffle',
# 	'Bowyer', 
# 	'Busch',
# 	'Gordon',
# 	'Patrick'
# ]
# 
# for name in names:
# 	print(name, '|', end=' ')
# 
# print('\nPrinting in reverse:')
# for name in reversed(names):
# 	print(name, '|', end=' ')

