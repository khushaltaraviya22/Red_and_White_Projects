Students = []


print("Welcome to the Student Data Organizer!\n")


while True: 

    print('\nSelect an option:')
    print('1. Add Student')
    print('2. Display All Students')
    print('3. Update Student Information')
    print('4. Delete Student')
    print('5. Display Subjects Offered')
    print('6. Exit')

    choice = int(input('Enter your choice:- '))

    match choice:
        case 1:
            print('\nEnter student details:')

            st = {
                'Student ID': int(input('Student ID:-  ')),
                'Name': input('Name:- '),
                'Age': int(input('Age:- ')),
                'Grade': input('Grade:- '),
                'DOB': input('Date of Birth (YYYY-MM-DD): '),
                'Subjects': input('Subjects (comma-separated): ')
            }

            Students.append(st)

            print('\nStudent added successfully!')

        case 2:

            print('\n--- Display All Students ---\n')

            for st in Students:
                for key, value in st.items():
                    print(f'{key}: {value}', end=' | ' )
                print('')

        case 3:

            id = int(input('\nEnter Student ID to Update it\'s Details:- '))

            for st in Students:
                if st['Student ID'] == id:

                    st['Name'] = input('Name:- ')
                    st['Age'] = int(input('Age:- '))
                    st['Grade'] = input('Grade:- ')
                    st['DOB'] = input('Date of Birth (YYYY-MM-DD): ')
                    st['Subjects'] = input('Subjects (comma-separated): ')

            print('\nStudent Details Updated Successfully.')


        case 4:
            id = int(input('\nEnter Student ID to Delete it\'s Details:- '))

            for st in Students:
                if st['Student ID'] == id:
                    Students.remove(st)

            print('\nStudent Details Deleted Successfully.')

        case 5:
            id = int(input('\nEnter Student ID to Display Subject Offered:- '))
            print('')
            for st in Students:
                if st['Student ID'] == id:
                    print(st['Subjects'])
        
        case 6:
            print('\nThank You\n')
            break
        case _:

            print('\nInvalid Choice\n')


