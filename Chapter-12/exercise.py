# Turn your Student class into a small Course class with attributes for course code and units, and a method that returns a formatted string.
class Course:
    def __init__(self, code, units):
        self.code = code
        self.units = units

    def classify(self):
        if self.units >= 3:
            return f"Since this {self.code} is a {self.units} course, it's important"
        return "Just keep on studying..."

subject = Course("CSC301", 3)
print(subject.classify())