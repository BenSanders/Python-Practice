x = int(input())

while x > 0:
	print(x % 2,end="")
	x = x // 2
print()

# if x > 0:
#     print(x % 2)
#     x = x / 2
# elif x == 0:
#     print("Number is 0")
# else:
#     print("Number is negative")