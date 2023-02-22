# avg_owls = 0.0
# 
# num_owls_zooA = int(input())
# num_owls_zooB = int(input())
# num_owls_zooC = int(input())
# 
# avg_owls = (num_owls_zooA + num_owls_zooB + num_owls_zooC / 3)
# 
# print('Average owls per zoo:', int(avg_owls))

# The above gets the average owls per zoo 4 but not sure how to get it to 2
# Oh, I see, needed the division integer be outside parenthesis

avg_owls = 0.0

num_owls_zooA = int(input())
num_owls_zooB = int(input())
num_owls_zooC = int(input())

avg_owls = (num_owls_zooA + num_owls_zooB + num_owls_zooC) / 3

print('Average owls per zoo:', int(avg_owls))