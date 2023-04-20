# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.
# 
# Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west. 

# Tip from CI Do an outer if/else to check for a valid vs invalid highway. Nest everything else inside the block where you’re dealing with a valid highway.
# (Checking for a valid vs invalid highway first should also help with the issue of those “even hundreds” highway numbers – they’re invalid regardless of whether they would otherwise be primary or aux.)

highway_number = int(input())

# valid or invalid?
if highway_number < 1 or highway_number > 999 or highway_number % 100 == 0: #invalid
	print("{} is not a valid interstate highway number." .format(highway_number))
else:
	# valid!
	if highway_number <= 99:
		# primary
		print("I-{} is primary, " .format(highway_number), end="")
		# print(f"I-{highway_number} is primary, ", end="")
	else:
		# aux
		print("I-{} is auxiliary, serving I-{}, " .format(highway_number,highway_number % 100), end="")
	
	if highway_number % 2 == 0:
		# even
		print("going east/west." .format(highway_number))
	else:
		# odd
		print("going north/south." .format(highway_number,highway_number % 100))