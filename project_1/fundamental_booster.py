print('Welcome to the Interactive Personal Data Collector! \n')

name = input('Please enter your name: ')
age = int(input('Please enter your age: '))
height = float(input('Please enter your height in meters: '))
favNum = int(input('Please enter your favorite number: '))

print('\nThank you! Here is the information we collected: \n')

print('Name: ' + name + ' ' + '(Type: ' + str(type(name)) + ', ' + ' Memory Address: ' + str(id(name)) + ')')
print('Age: ' + str(age) + ' ' + '(Type: ' + str(type(age)) + ', ' + ' Memory Address: ' + str(id(age)) + ')')
print('Height: ' + str(height) + ' ' + '(Type: ' + str(type(height)) + ', ' + ' Memory Address: ' + str(id(height)) + ')')
print('Favorite Number: ' + str(favNum) + ' ' + '(Type: ' + str(type(favNum)) + ', ' + 'Memory Address: ' + str(id(favNum)) + ')' + '\n')

print('Your birth year is approximately: ' + str(age) + ' based on your age of ' + str(2026 - age) + ' \n')

print('Thank you for using Personal Data Collector. Goodbye!')