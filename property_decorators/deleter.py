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

    @fullname.setter
    def fullname(self, new_name: str):
        first, last = new_name.split(" ")
        self.first = first
        self.last = last

    @fullname.deleter
    def fullname(self):
        print("\nDeleting FullName!")
        self.first = ""
        self.last = ""


emp = Employee("Atanu", "Ghosh", 1000)

emp.fullname = "Arunavo Mukherjee"

print(emp.first)
print(emp.email)
print(emp.fullname)

del emp.fullname
print("Current FullName :", emp.fullname)
