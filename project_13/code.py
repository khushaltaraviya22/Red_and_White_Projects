class Employee:
    def __init__(self, emp_id=0, name="Unknown", age=0, salary=0):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.__salary = salary 

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        if salary >= 0:
            self.__salary = salary
        else:
            print("Salary cannot be negative!")

    def display(self):
        print(f"""
Employee Details:
              
Name: {self.name}
Age: {self.age}
Employee ID: {self.emp_id}
Salary: ${self.__salary}
""")


class Manager(Employee):
    def __init__(self, emp_id=0, name="Unknown", age=0, salary=0, department="General"):
        super().__init__(emp_id, name, age, salary)
        self.department = department

    def display(self):
        print(f"""
Manager Details:
              
Name: {self.name}
Age: {self.age}
Employee ID: {self.emp_id}
Salary: ${self.get_salary()}
Department: {self.department}
""")


class Developer(Employee):
    def __init__(self, emp_id=0, name="Unknown", age=0, salary=0, language="Python"):
        super().__init__(emp_id, name, age, salary)
        self.language = language

    def display(self):
        print(f"""
Developer Details:
              
Name: {self.name}
Age: {self.age}
Employee ID: {self.emp_id}
Salary: ${self.get_salary()}
Programming Language: {self.language}
""")


employees = []
managers = []
developers = []


def create_employee():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))

    emp = Employee(emp_id, name, age, salary)
    employees.append(emp)

    print(f"\nEmployee created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}\n")


def create_manager():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    department = input("Enter Department: ")

    mgr = Manager(emp_id, name, age, salary, department)
    managers.append(mgr)

    print(f"\nManager created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, department: {department}\n")


def create_developer():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    emp_id = input("Enter Employee ID: ")
    salary = float(input("Enter Salary: "))
    language = input("Enter Programming Language: ")

    dev = Developer(emp_id, name, age, salary, language)
    developers.append(dev)

    print(f"\nDeveloper created with name: {name}, age: {age}, ID: {emp_id}, salary: ${salary}, department: {language}\n")


def show_details():
    print("\n1. Employee")
    print("2. Manager")
    print("3. Developer")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            if not employees:
                print("No employees found!\n")
            else:
                for emp in employees:
                    emp.display()

        case 2:
            if not managers:
                print("No managers found!\n")
            else:
                for mgr in managers:
                    mgr.display()

        case 3:
            if not developers:
                print("No developers found!\n")
            else:
                for dev in developers:
                    dev.display()

        case _:
            print("Invalid choice!\n")


def menu():

    print('\n--- Python OOP Project: Employee Management System ---')

    while True:

        print("""
Choose an operation:
1. Create an Employee
2. Create a Manager
3. Create a Developer
4. Show Details
5. Exit
""")

        choice = int(input("Enter your choice: "))

        match choice:
            case 1:
                create_employee()
                print('\n--- Choose another operation ---\n')
            case 2:
                create_manager()
                print('\n--- Choose another operation ---\n')
            case 3:
                create_developer()
                print('\n--- Choose another operation ---\n')
            case 4:
                show_details()
                print('\n--- Choose another operation ---\n')
            case 5:
                print("\nExiting  the system. All resources have been freed\n")
                print("Goodbye!")
                break
            case _:
                print("Invalid choice! Try again.\n")


menu()