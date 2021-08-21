class Employee:

    raise_amount = 1.04
    num_of_employees = 0

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay

        Employee.num_of_employees += 1

    def fullname(self) -> str:
        return self.first + " " + self.last

    def email(self) -> str:
        return (self.first + "." + self.last + "@company.com").lower()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)

    def __repr__(self) -> str:
        return "Employee('{}', '{}', '{}')".format(self.first, self.last, self.pay)

    def __str__(self) -> str:
        return "{} - {}".format(self.fullname(), self.email())


e1 = Employee("Atanu", "Ghosh", 1000)
e2 = Employee("Test", "User", 2000)

print(repr(e1))
print(str(e1))

print(e1.__repr__())
print(e1.__str__())
