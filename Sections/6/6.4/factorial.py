N = int(input())  # Read user-entered number
total = N

i = total - 1
# Initialize the loop variable

while i > 1:
	# Set total to total * (i)
	total = total * i
	# Decrement i
	i -= 1

print(total)
