# Write multiple if statements:
# If car_year is before 1967, print "Probably has few safety features." (without quotes).
# If after 1971, print "Probably has head rests.".
# If after 1990, print "Probably has electronic stability control.".
# If after 2000, print "Probably has tire-pressure monitor.".
# End each phrase with period and newline. Remember that print() automatically adds a newline. 
# Ex: car_year = 1995 prints:
# 
# Probably has head rests.
# Probably has electronic stability control.

car_year = int(input())

#car_year before 1967 probably has few safety features
if car_year < 1967:
	print('Probably has few safety features.')
#after 1971 probably has head rests
if car_year > 1971:
	print('Probably has head rests.')
#after 1990 probably has electronic stability control
if car_year > 1990:
	print('Probably has electronic stability control.')
#after 2000 probably has tire-pressure monitor
if car_year > 2000:
	print('Probably has tire-pressure monitor.')
