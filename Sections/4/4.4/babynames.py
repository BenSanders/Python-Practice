print('This program will remove names from this list')

male_names = { 'Oliver', 'Declan', 'Henry' }
print(male_names)

name_to_remove = input('Name to remove: ')
name_to_add = input('Name to add: ')

male_names.remove(name_to_remove)
male_names.add(name_to_add)

print(male_names)