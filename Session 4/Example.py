class Student:

    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.lunch_status = False

    def reservation(self):
        
        if self.lunch_status:
            print(f"{self.name}, you have lunch today.")
        else:
            print(f"{self.name}, you don't have lunch today.")


    def reserve(self):

        if self.lunch_status:
            print(f"{self.name}, you have reserved before.")
        else:
            self.lunch_status = True
            print(f"{self.name}, your lunch is reserved.")

    def reserve_cancel(self):

        if self.lunch_status:
            self.lunch_status = False
            print(f"{self.name}, your reservation canceld.")
        else:
            print(f"{self.name}, you don't have reservation today.")



s1 = Student('Morteza', 65165845)

s1.reserve()

s1.reservation()

s1.reserve_cancel()

s1.reservation()

