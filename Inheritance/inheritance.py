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
        return (self.first + "." + self.last + "@company.com").lower()

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)


class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang) -> None:
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employee_list=None) -> None:
        super().__init__(first, last, pay)
        if employee_list is None:
            self.employee_list = []
        else:
            self.employee_list = employee_list

    def add_emp(self, emp):
        if emp not in self.employee_list:
            self.employee_list.append(emp)

    def remove_emp(self, emp):
        if emp in self.employee_list:
            self.employee_list.remove(emp)

    def print_emps(self):
        for emp in self.employee_list:
            print("-->", emp.fullname())


d1 = Developer("Atanu", "Ghosh", 1000, "Python")
d2 = Developer("Test", "User", 2000, "Java")

m1 = Manager("Sue", "Smith", 10000, [d1])

print(isinstance(m1, Employee))
print(isinstance(m1, Manager))
print(isinstance(m1, Developer))

print(issubclass(Developer, Employee))
print(issubclass(Manager, Employee))
print(isinstance(Developer, Manager))
