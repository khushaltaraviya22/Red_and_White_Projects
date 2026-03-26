# Example of inheritance

#================ Single Level Inheritance ================


# class Parent:

#     name = 'Test'

#     def greet(self):
#         print('Greeting from parent')


# class Child(Parent):
#     pass


# object = Child()

# print(object.name)


# object.greet()

#================ Multilevel Inheritance ================


# class GrandParent:

#     def grandGreet(self):
#         print('Greeting from grand parent')


# class Parent(GrandParent):

#     name = 'Test'

#     def greet(self):
#         print('Greeting from parent')


# class Child(Parent):
#     pass


# object = Child()

# print(object.name)


# object.greet()
# object.grandGreet()



#================ Multiple Inheritance ================


# class Father:

#     def fartherGreet(self):
#         print('Greeting from Father')


# class Mother:

#     name = 'Test'

#     def motherGreet(self):
#         print('Greeting from Mother')


# class Child(Father, Mother):
#     pass


# object = Child()

# print(object.name)

# object.fartherGreet()
# object.motherGreet()



#================ Hierarchical Inheritance ================


# class Father:

#     def fartherGreet(self):
#         print('Greeting from Father')


# class Mother:

#     name = 'Test'

#     def motherGreet(self):
#         print('Greeting from Mother')


# class Child(Father, Mother):
#     pass

# class Child2(Father, Mother):
#     pass

# object = Child()
# object2 = Child2()


# print(object.name)

# object.fartherGreet()
# object.motherGreet()

# print()

# object2.fartherGreet()
# object2.motherGreet()

