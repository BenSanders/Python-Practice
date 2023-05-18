input_month = input()
input_day = int(input())

#31 days January, March, May, July, August, October, and December
#30 days September, April, June November
#The dates for each season are:
#Spring: March 20 - June 20
#Summer: June 21 - September 21
#Autumn: September 22 - December 20
#Winter: December 21 - March 19

months_of_31 = ["January", "March", "May", "July", "August", "October","December"]
months_of_30 = ["September", "April", "June", "November"]


if(input_month in months_of_31 and 0 < input_day <= 31) or (input_month in months_of_30 and 0 < input_day <= 30) or (input_month == "February" and 0 < input_day <= 29):
	if(input_month == "April" or input_month == "May") or (input_month == "March" and input_day >= 20) or (input_month == "June" and input_day <= 20):
		# March 20 - June 20
		print("Spring")
	elif(input_month == "July" or input_month == "August") or (input_month == "June" and input_day >= 21) or (input_month == "September" and input_day <= 21):
		# June 21 - September 21
		print("Summer")
	elif(input_month == "October" or input_month == "November") or (input_month == "September" and input_day >= 22) or (input_month == "December" and input_day <= 20):
		# September 22 - December 20
		print("Autumn")
	elif(input_month == "January" or input_month == "February") or (input_month == "December" and input_day >= 21) or (input_month == "March" and input_day <= 19):
		# December 21 - March 19
		print("Winter")
else:
	print('Invalid')

