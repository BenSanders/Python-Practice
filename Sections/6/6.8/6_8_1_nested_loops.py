c1 = 'a'
while c1 < 'b':
	c2 = 'a'
	while c2 <= 'c':
		print('{}{}'.format(c1, c2), end=' ')
		c2 = chr(ord(c2) + 1)
	c1 = chr(ord(c1) + 1)
	
	# Correct
	# aa ab ac 
	# Outer loop executes once ("a"). Inner loop executes three times ("a", "b", "c").
	
	i1 = 1
	while i1 < 19:
		i2 = 3
		while i2 <= 9:
			print('{}{}'.format(i1,i2), end=' ')
			i2 = i2 + 3
		i1 = i1 + 10
		
	# Correct
	# 13 16 19 113 116 119 
	# outer loop: i1 = 1,11 inner loop: i2=3,6,9 i1 cannot exceed 19 so the outer loop only runs twice. i2 cannot exceed 9 so the inner loop will run 3 times.

