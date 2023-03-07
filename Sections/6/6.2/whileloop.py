#  Write a while loop that repeats while user_num ≥ 1. In each loop iteration, first divide user_num by 2, then print user_num.
# 
# Sample output with input: 20
# 
# 10.0
# 5.0
# 2.5
# 1.25
# 0.625

user_num = int(input())
i = 1

while i <= user_num :
	# divide user_num by 2
	user_num / 2
	# print user_num
	print(i)
	# increment number
	i += 1