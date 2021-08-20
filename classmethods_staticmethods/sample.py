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

    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount

    @classmethod
    def from_string(cls, emp_str: str):
        first, last, pay = emp_str.split("-")
        return cls(first, last, pay)

    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee("Atanu", "Ghosh", 1000)
emp_2 = Employee("Test", "User", 2000)

emp_1.set_raise_amt(1.05)

emp_str_1 = "Atanu-Ghosh-3000"
emp_str_2 = "Corey-Schafer-4000"
emp_str_3 = "Dorian-Dotslash-5000"

new_emp_1 = Employee.from_string(emp_str_1)
new_emp_2 = Employee.from_string(emp_str_2)

print(new_emp_2.fullname())
print(new_emp_2.email())

import datetime
my_date = datetime.date(2021, 8, 23)

print(Employee.is_workday(my_date))
