# Primary U.S. interstate highways are numbered 1-99. Odd numbers (like the 5 or 95) go north/south, and evens (like the 10 or 90) go east/west. Auxiliary highways are numbered 100-999, and service the primary highway indicated by the rightmost two digits. Thus, I-405 services I-5, and I-290 services I-90.
# 
# Given a highway number, indicate whether it is a primary or auxiliary highway. If auxiliary, indicate what primary highway it serves. Also indicate if the (primary) highway runs north/south or east/west. 

# Tip from CI Do an outer if/else to check for a valid vs invalid highway. Nest everything else inside the block where you’re dealing with a valid highway.

highway_number = int(input())

if (highway_number < 1 or highway_number > 999) :
	# if yes, the highway number is invalid
	print(str(highway_number) + " is not a valid interstate highway number")
else :
	# This checks if highway number is less than 100
	if (highway_number < 100) :
		if (highway_number % 2 == 0) :
			# Even highway number are primary going east/west
			print("I-" + str(highway_number) + " is primary, going east/west.")
		else :
			# Odd highway number going north/south
			print("I-" + str(highway_number) + " is primary, going north/south.")
	else :
		if ((highway_number % 100) % 2 == 0) :
			# Even highway number are auxiliary going east/west
			print("I-" + str(highway_number) + " is auxiliary, serving going east/west.")
		else :
			# Even highway number going north/south
			print("I-" +str(highway_number) + " is auxilary, going north/south.")

# First attempt
# if (highway_number <= 1) AND (highway_number >= 99) : # Primary 1-99 and aux are 100-999
# 	if highway_number % 2 :
# 		# Odd
# 		print('Highway goes north/south')
# 	else :
# 		#Even
# 		print('Highway goes east/west')
# first check for primary or aux highway
# 	if aux highway indicate primary highway it serves
# 		indicate if the primary highway runs north/south or east west
	
# if file exists(path_to_file) then :
# 	open (path_to_file)
# 	for each line in file : print the line of the file
# else :
# 	print this file doesn't exist