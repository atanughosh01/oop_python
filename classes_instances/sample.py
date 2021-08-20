class Employee:
    
    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"


emp_1 = Employee("Atanu", "Ghosh", 1000)
emp_2 = Employee("Test", "User", 2000)

print(emp_1.email)
print(emp_2.email)
