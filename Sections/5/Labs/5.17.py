# need two inputs par and player's stroke number
# input par
par = int(input())
# input player's stroke number
stroke = int(input())

# if par != 3, 4, or 5 print error
if not 2 < par < 6:
	print('Error')
elif stroke == (par - 2):
	print('Eagle')
elif stroke == (par - 1):
	print('Birdie')
elif stroke == par:
	print('Par')
elif stroke == (par + 1):
	print('Bogey')
else:
	print('Error')