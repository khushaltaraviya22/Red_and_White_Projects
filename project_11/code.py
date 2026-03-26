# Constructor inheritance


class Mahindra:

    def __init__(self, seats, ac):        
        self.seats = seats
        self.ac = ac

class Xuv(Mahindra):


    def __init__(self, seats, ac, modelName):
        super().__init__(seats, ac)
        self.modelName = modelName

    
    def getData(self):

        print(f'''
Model:- {self.modelName},
Seats:- {self.seats},
AC:- {self.ac}''')
        

obj1 = Xuv(5,True, 'XUV300')
obj2 = Xuv(7,True, 'XUV700')


obj1.getData()
obj2.getData()
