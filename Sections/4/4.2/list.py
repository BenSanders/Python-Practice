# list.append(value) # Adds value to the end of a list Ex: my_list.append('abc')
# list.pop(i) # Removes the element at index i from list Ex: my_list.pop(1)
# list.remove(v) # Removes the first element whose value is v Ex: my_list.remove('abc')

my_list = [10, 'bw']
print(my_list)

my_list.append('abc')
print('After append:', my_list)

my_list.pop(1)
print('After pop:', my_list)

my_list.remove('abc')
print('After remove:', my_list)

# Write a statement that performs the desired action. Assume the list
# house_prices = ['$140,000','$550,000','$480,000'] exists

# 1) Update the price of the second item in house_prices to '$175,000'.
'''
First lets figure out what the target new price is for the second item by
subtracting '$175,000' from '$550,000' to get what I need to subtract for
it to be '$175,000'.

Never mind I was overthinking it like a dummy. The answer is house_prices = '$175,000'
'''