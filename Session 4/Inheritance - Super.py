class Vichle: # Parent
    def __init__(self, name, year):
        self.name = name
        self.year = year

    def printname(self):
        print(self.name , self.year)


class Car(Vichle): # Child
    def __init__(self, name, year, num_ch):
        super().__init__(name, year)
        self.num_ch = num_ch

    def printYear(self):
        print(self.year)
        

v1 = Vichle('Ford', 1980)
c1 = Car('Volvo', 2014, 6)

c1.printname()
c1.printYear()
