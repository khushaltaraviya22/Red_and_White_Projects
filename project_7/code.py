# Exmaple of class and object


# class Student:

#     name = 'Test'
#     city = 'Rajkot'

#     def display(self):
#         print('hello')

# obj = Student()

# obj.display()
# print(obj.name)
# print(obj.city)

# Exmaple of getter and setter


class Person:

    __name = None
    __age = None

    def setData(self,name,age):
    
        self.__name = name
        self.__age = age
    
    def getData(self):
        
        print(f'Name:- {self.__name}, Age:- {self.__age}')


one = Person()
two = Person()


one.setData('Jay', 21)
two.setData('Yash',25)

# if you want to delete any object 
# del one

one.getData()
two.getData()

