# Real life example of hierarchical inheritance


class Employee :

    def __init__(self,empId,name,city):
        self.empId = empId
        self.name = name
        self.city = city


class Manager(Employee):

    def __init__(self, empId, name, city, department):
        super().__init__(empId, name, city)
        self.department = department

    def getManagerInfo(self):

        print(f'''
Id:- {self.empId},
Name:- {self.name},
City:- {self.city},
Department:- {self.department}''')
        

class Developer(Employee):

    def __init__(self, empId, name, city, pro_lan):
        super().__init__(empId, name, city)
        self.pro_lan = pro_lan

    def getDeveloperInfo(self):

        print(f'''
Id:- {self.empId},
Name:- {self.name},
City:- {self.city},
Programmin Language:- {self.pro_lan}''')
        


obj1 = Manager(1,'Yash','Rajkot','IT')
obj2 = Developer(12,'John','London','Python')


obj1.getManagerInfo()
obj2.getDeveloperInfo()
