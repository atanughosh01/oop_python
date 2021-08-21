# class Employee:

#     num_of_employees = 0

#     def __init__(self, first: str, last: str, pay: int) -> None:
#         self.first = first
#         self.last = last
#         self.pay = pay
#         # self.fullname = first + " " + last

#         Employee.num_of_employees += 1

#     def fullname(self) -> str:
#         return self.first + " " + self.last

#     def email(self) -> str:
#         return (self.first + "." + self.last + "@domain.com").lower()


# emp = Employee("Atanu", "Ghosh", 1000)

# emp.first = "Arunavo"

# print(emp.first)
# print(emp.email())
# print(emp.fullname())

class Employee:

    num_of_employees = 0

    def __init__(self, first: str, last: str, pay: int) -> None:
        self.first = first
        self.last = last
        self.pay = pay
        # self.fullname = first + " " + last

        Employee.num_of_employees += 1

    @property
    def fullname(self) -> str:
        return self.first + " " + self.last

    @property
    def email(self) -> str:
        return (self.first + "." + self.last + "@domain.com").lower()


emp = Employee("Atanu", "Ghosh", 1000)

emp.first = "Arunavo"

print(emp.first)
print(emp.email)
print(emp.fullname)
