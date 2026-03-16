sId = 1

Students = []


while True:

    print('\nWelcome to Student Form\n')

    print('Enter 1 to Add')
    print('Enter 2 to View')
    print('Enter 3 to Update')
    print('Enter 4 to Delete')
    print('Enter 0 to Exit\n')

    choice = int(input('Enter your choice:- '))

    match choice:
        case 1:
            st = {
                'Id': sId,
                'Name': input('\nEnter Student Name:- '),
                'Age': int(input('Enter Student Age:- ')),
                'City': input('Enter Student City:- ')
            }
            Students.append(st)
            sId+=1
            print('\nStudent Added Successfully!\n')
        case 2:
            id = int(input('Enter Student ID to View it\'s Data:- '))

            for st in Students:
                if st['Id'] == id:

                    for key,value in st.items():
                        print(f'Student {key}:- {value}')
        case 3:
            id = int(input('Enter Student ID to Update it\'s Data:- '))

            for st in Students:
                if st['Id'] == id:
                    st['Name'] = input('Enter Student Name:- ')
                    st['Age'] = int(input('Enter Student Age:- '))
                    st['City'] = input('Enter Student City:- ')
            
            print('\nStudent Updated Successfully.\n')

        case 4:
            id = int(input('Enter Student ID to Delete it\'s Data:- '))

            for st in Students:
                if st['Id'] == id:
                    Students.remove(st)

            print('\nStudent Deleted Successfully.\n')

        case 0:
            print('\nThank You!\n')
            break
        case _:
            print('Invalid Choice.')


