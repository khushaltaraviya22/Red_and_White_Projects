#Example of Constructor and Destructore

# class Student:

    # def __init__(self, name, age, city):

        # self.name = name
        # self.age = age
        # self.city = city

        # print(f'Name:- {self.name}, Age:- {self.age}, City:- {self.city}')

    # def getData(self):

    #     print(f'Name:- {self.name}, Age:- {self.age}, City:- {self.city}')

    # def __del__(self):

        # print('Destructor called')


# obj = Student('Test',30,'Rajkot')
# obj2 = Student('Test1',38,'Mumbai')


# obj.getData



#=========== Bank ===============


class Bank:

    def __init__(self, name, ac_no, balance):

        self.name = name
        self.ac_no = ac_no
        self.balance = balance


        print(f'\nYour account number is:- {self.ac_no}')
        print('Account Created Successfully !')


    def deposite(self, ac_no, amount):
    
        self.ac_no = ac_no
        self.balance += amount

        print('\nAmount added to your account successfully !\n')

    def withdraw(self, ac_no, amount):

        self.ac_no = ac_no

        if self.balance >= amount:
            self.balance -= amount
        else:
            print('Low balance! Please add balance')

        print('\nAmount Withdraw Successfully !\n')

    def getBalance(self):
        
        print(f'\nCurrent Balance:- {self.balance}\n')


bank1 = Bank('Test', 202020, 100000)


print('\nWelcome to our bank !\n')

while True:

    print('Enter 1 to desposite amount')
    print('Enter 2 to withdraw account')
    print('Enter 3 to check current balance')
    print('Enter 0 to exit\n')


    choice = int(input('Enter your choice:- '))

    match choice:

        case 1:
            ac_num = int(input('Enter your accoount number:- '))
            amount = int(input('Enter amount:- '))
            print()
            bank1.deposite(ac_num ,amount)

        case 2:
            ac_num = int(input('Enter your accoount number:- '))
            amount = int(input('Enter amount:- '))
            print()
            bank1.withdraw(ac_num, amount)

        case 3:
            bank1.getBalance()

        case 0:
            print('\nThank you!\n')
            break
        case _:
            print('\nInvalid choice\n')



