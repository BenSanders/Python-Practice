temperatures = [30,20,2,-5,-15,-8,-1,0,5,35]

num_neg = 0
for temp in temperatures:
	if temp < 0:
		num_neg += 1
		print(num_neg)