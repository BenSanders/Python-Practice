is_leap_year = False
   
input_year = int(input())

# figure it out
if input_year % 4 == 0:
	# don't kneow yet...
	if input_year % 100 == 0:
		# still don't know
		if input_year % 400 == 0: # 1600, 2000
			is_leap_year = True
		else: # 1700, 1800, 1900
			is_leap_year = False
	else: # most leap years.. 2016, 1712, etc
		is_leap_year = True
else:
	is_leap_year = False

if is_leap_year == True:
	print(input_year, '- leap year')
else:
	print(input_year,'- not a leap year')