# These will error out
num_dogs = "Black Lab"

print(num_dogs). #Error from the period at the end
print("Dogs:"num_dogs) #Error from missing a comma
print('Woof!") 
#Mismatched quotes

print(Woof!) # Needs quotes
print("Hello + friend!") #Runs perfectly fine

triangle_base = 0 # Triangle base (cm)
triangle_height = 0 #Triangle height (cm)
triangle_area = 0 # Triangle area (cm)

print("Enter triangle base(cm):")
triangle_base = int(input())

print("Enter triangle height(cm):")
triangle_height = int(input())

# Calculate triangle area

triangle_area = (triangle_base*triangle_height)/2 # Print out the triangle base, height, and area

print('Triangle_area=(',end=''))
print(triangle_base)

print('*',end='')

print(triangle_height, end='')
print(')/2=',end='')
print(triangle_area,end='')
print('cm**2')

"""
Error type 		|	Description
SyntaxError		|	The program contains invalid code that cannot be understood
IndentionError	|	The lines of the program are not properly indented
ValueError		|	An invalid value is used - can occur if giving letters to in()
NameError		|	The program tries to use a variable that does not exist
TypeError		|	An operation uses incorrect types - can occur if adding an integer to a string
"""

# A logic error is often called a bug

current_salary = int(input('Enter current salary:'))

raise_percentage = 5  # Logic error gives a 500% raise instead of 5%.
new_salary = current_salary + (current_salary * raise_percentage)
print('New salary:', new_salary)

print("Predictions are hard.")
print("Especially about the future.")
user_num = 5
print('user_num is: ' user_num)