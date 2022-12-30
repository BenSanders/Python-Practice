print('Hello world!')

# Each print statement starts with a new line
print('Hello there.')
print('My name is...')
print('Carl?')

print('3 2 1 Go!')

print('*****')
print('*   *')
print('*****')
print('*   *')
print('*****')

# including end=' ' keeps output on the same line
print('Hello there.', end=' ')
print('My name is...', end=' ')
print('Carl?')

# Printing the value of a variable
wage = 20

print('Wage is', end=' ')
print(wage) # print variable's value
print('Goodbye.')

# Printing multiple items using a single print statement
wage = 20

print('Wage:', wage) # Comma separates multiple items
print('Goodbye.')

# Newline character
print('1\n2\n3\n')

# Printing without text
print('123')
print()
print('abc')

country_population = 1344130000
country_name = "China"

print('The population of', end=' ')
print(country_name, end=' ')
print('was', end=' ')
print(country_population, end=' ')
print('in 2011')

# Input which breakks the above because it's setting a variable that will be used for country lol
my_var = input()
print(my_var)

# Convert strings to integers
my_string = '123'
my_int = int('123')

print(my_string)
print(my_int)