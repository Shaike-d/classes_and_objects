class Student():
    def __init__(self,name):
        self.name = name
        self.graides = []

    def add_grade(self,grade):
        return self.graides.append(grade)

    def average(self):
        if len(self.graides) == 0:
            return 0
        else:
            return sum(self.graides)/len(self.graides)

    def __str__(self):
        return f"{self.name} (average {self.average()})"

def action():
    dana = Student("Dana")
    print(dana.average())
    dana.add_grade(90)
    dana.add_grade(75)
    print(dana.average())
    print(dana)
        
