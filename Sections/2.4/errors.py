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