class Student:
    def __init__(self, name, gpa):
        self.name = name
        self.gpa = gpa

    def classify(self):
        if self.gpa >= 4.5:
            return "First Class"

me = Student("Data Muse", 4.5)
print(me.classify())