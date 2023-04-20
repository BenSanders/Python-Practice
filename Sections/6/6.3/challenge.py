# Almost have it
# num_insects = int(input()) # Must be >= 1
# 
# while num_insects * 2 <= 100:
#    if num_insects > 0:
# 	  num_insects *= 2
# 	  print(num_insects, " ")

# Given positive integer num_insects, write a while loop that prints, then doubles, num_insects each iteration. Print values ≤ 100. Follow each number with a space.
# 
# Sample output with input: 8
# 
# 8 16 32 64

num_insects = int(input()) # Must be >= 1


while num_insects <= 100:
	print(num_insects, end=' ')
	num_insects *= 2