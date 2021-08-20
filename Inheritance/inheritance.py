class Employee:
    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first, last, pay) -> None:
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self):
        return self.first + " " + self.last

    def email(self):
        return self.first + "." + self.last + "@company.com"

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    pass


d1 = Developer("Atanu", "Ghosh", 1000)
d2 = Developer("Test", "User", 2000)

print(d1.email())
print(d2.email())

print(help(Developer))
