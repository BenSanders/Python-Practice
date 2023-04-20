# Slice notation also provides for a third argument, known as the stride. The stride determines how much to increment the index after reading each element. For example, my_str[0:10:2] reads every other element between 0 and 10. The stride defaults to 1 if not specified. 

numbers = '0123456789'

print('All numbers: {}'.format(numbers[::]))
print('Every even number: {}'.format(numbers[::2]))
print('Every third number between 1 and 8: {}'.format(numbers[1:9:3]))