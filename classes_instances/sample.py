class Employee:
    
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"

    def fullname(self):
        return (self.first + " " + self.last)


emp_1 = Employee("Atanu", "Ghosh", 1000)
emp_2 = Employee("Test", "User", 2000)

print(emp_1.email)
print(emp_2.email)

print(emp_1.fullname())
print(emp_2.fullname())

print(Employee.fullname(emp_1))
print(Employee.fullname(emp_2))
