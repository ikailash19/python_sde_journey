class Student:

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def is_pass(self):
        return self.marks>=35

s1 = Student("Kailash", 80)
print(s1.is_pass())