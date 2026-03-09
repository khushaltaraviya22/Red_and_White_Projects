print('\nWelcome to the pattern Generator and Number Analyzer!\n')

print('Select an option:')
print('1. Generate a pattern')
print('2. Analyze a Range of Numbers')
print('3. Exit')
choice = input('Enter your choice: ')

if(choice == '1'):
    rows = int(input('\nEnter the number of rows for the pattern: '))

    print('\nPattern:')

    for i in range(1, rows + 1):
        print('* ' * i)

elif(choice == '2'):
    start = int(input('\nEnter the start of the range: '))
    end = int(input('Enter the end of the range: '))

    sum = 0

    for i in range(start, end + 1):
        if(i % 2 == 0):
            print('Number '+ str(i) +' is Even')
        else:
            print('Number '+ str(i) +' is Odd')
        sum = int(sum+i)

    print('Sum of all numbers from ' + str(start) + ' to ' + str(end) + ' is ' + str(sum))

else:    
    print('\nExiting the program. Goodbye!')