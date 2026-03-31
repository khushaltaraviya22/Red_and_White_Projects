class Employee :

    def __init__(self,empId,name,city):
        self.empId = empId
        self.name = name
        self.city = city
        

    def getInfo(self):
        print(f'''
Id:- {self.empId},
Name:- {self.name},
City:- {self.city}
''')


class Manager(Employee):

    def __init__(self, empId, name, city, department):
        super().__init__(empId, name, city)
        self.department = department
        print('Manager Created Successfully !\n')

    def getInfo(self):
        super().getInfo()
        print(f'The manager is from {self.department}\n')
        

class Developer(Employee):

    def __init__(self, empId, name, city, pro_lan):
        super().__init__(empId, name, city)
        self.pro_lan = pro_lan
        print('Developer Created Successfully !\n')

    def getInfo(self):
        super().getInfo()
        print(f'The Developer domain is {self.pro_lan}\n')



e_list = []
m_list = []
d_list = []


while True:

    print('Enter 1 to create employee')
    print('Enter 2 to create manager')
    print('Enter 3 to create developer')
    print('Enter 4 to view\n')


    try :
        choice  = int(input('Enter your choice:- '))
        print('')
    except ValueError:
        
        print('Please enter valid choice.')

    else: 
        match choice:
            case 1:
                id = len(e_list)+1
                eObj = Employee(id,'John','Rajkot')
                print('Employee Created Successfully !\n')
                e_list.append(eObj)
            case 2:
                id = len(m_list)+1
                mObj = Manager(id,'John','Rajkot','IT')
                m_list.append(mObj)
            case 3:
                id = len(d_list)+1
                dObj = Developer(id,'John','Rajkot','Python')
                d_list.append(dObj)
            case 4:
                ch = int(input('Enter 1,2,3 to view respectibely data for Employee, Manager, Developer:- '))
            
                if ch == 1:
                    for e in e_list:
                        e.getInfo()
                elif ch == 2:  
                    for m in m_list:
                        m.getInfo()
                elif ch == 3:   
                    for d in d_list:
                        d.getInfo()
                else:
                    print('Invalid choice')

            case _:
                print('Invalid choice')