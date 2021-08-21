class Employee:

    raise_percent = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return self.first + " " + self.last

    def email(self):
        return (self.first + "." + self.last + "@company.com").lower()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_percent)


emp_1 = Employee("Atanu", "Ghosh", 1000)
emp_2 = Employee("Test", "User", 2000)

print(emp_1.fullname())
print(emp_1.email())
print(emp_1.pay)
emp_1.apply_raise()
print(emp_1.pay)

print("----------------------------")

print(emp_2.fullname())
print(emp_2.email())
print(emp_2.pay)
emp_2.apply_raise()
print(emp_2.pay)


print(Employee.num_of_employees)
