# Example of CRUD operation

# list = []

# while True:

#     print('Enter 1 to Add')
#     print('Enter 2 to Read')
#     print('Enter 3 to Update')
#     print('Enter 4 to Delete\n')

#     choice = int(input('Enter your choice:- '))

#     try:
#         match (choice):
#             case 1: 
#                 list.append(int(input('\nEnter valye to Add:- ')))
#                 print(f'{list}\n')
#                 # print(list + '\n')
#             case 2:
#                 for i in list:
#                     print(i)
#                 print()
#             case 3: 
#                 ind = int(input('\nEnter index to Update:- '))
#                 list[ind] = int(input('Enter value to Update:- '))
#                 print(f'{list}\n')
#             case 4:
#                 val = int(input('\nEnter value to Delete:- '))
#                 list.remove(val)
#                 print(f'{list}\n')
#             case _:
#                 print('\nSorry!, Invalid choice you have entered\n')
#     except:
#         print('\nError occured\n')



# Example of Dictonary

di = {
    'Name': 'Test',
    'Age': 20,
    'Subject': ['Hindi','English'],
    'Status': True
}


# print(di)
# print(di['Name'])
# print(di['Subject'][1])


# for key,value in di.items():
#     print(f"{key}:- {value}")

# di["City"] = "Rajkot"
# di['Age'] = 25

# print(di)


# del di['Status']

# print(di)

print(di.get('hello','not found'))
            

