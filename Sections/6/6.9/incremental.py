# First version
user_input = input('Enter phone number: ')

index = 0
for character in user_input:
	print('Element {} is: {}'.format(index, character))
	index += 1
	
# Second version
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
	if '0' <= character <= '9':
		phone_number += character
	else:
		#FIXME: Add elif branches for letters and hyphen
		phone_number += '?'

print('Numbers only: {}'.format(phone_number))

# Third Version
user_input = input('Enter phone number: ')
phone_number = ''

for character in user_input:
	if ('0' <= character <= '9') or (character == '-'):
		phone_number += character
	elif ('a' <= character <= 'c') or ('A' <= character <= 'C'):
		phone_number += '2'
	#FIXME: Add remaining elif branches
	else:
		phone_number += '?'

print('Numbers only: {}'.format(phone_number))

# Fourth Version
Enter phone number (letters/- OK, no spaces): 1-555-HOLIDAY       
Numbers only: 1-555-4654329
...
Enter phone number (letters/- OK, no spaces): 1-555-holiday
Numbers only: 1-555-4654329
...
Enter phone number (letters/- OK, no spaces): 999-9999
Numbers only: 999-9999
...
Enter phone number (letters/- OK, no spaces): 9876zywx%$#@
Numbers only: 98769999????