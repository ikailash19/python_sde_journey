class Employee:

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def increment(self):
        self.salary += 5000

emp = Employee("Kailash", 45000)
print(emp.salary)
emp.increment()
print(emp.salary)