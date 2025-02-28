class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, age):
        Person.__init__(self, fname, lname)
        self.age = age

x = Student('Aslan', 'Rasouli', 25)
x.printname()