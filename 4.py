class Employee:
    def __init__(self, id, firstName, lastName, salary) -> None:
        self.id = id
        self.firstName = firstName
        self.lastName = lastName
        self.salary = salary

    def det_id(self):
        return self.id

    def get_fName(self):
        return self.firstName

    def get_lName(self):
        return self.lastName

    def get_Name(self):
        return f"{self.firstName} {self.lastName}"

    def get_salary(self):
        return self.salary

    def set_salary(self, new_salary):
        self.salary = new_salary

    def get_annualSalary(self):
        return self.salary * 12

    def raise_Salary(self, percent):
        self.salary *= (1 + percent / 100)
        return self.salary

    def det_info(self):
        print(f"ID: {self.id}")
        print(f"Ismi: {self.firstName}")
        print(f"Familiyasi: {self.lastName}")
        print(f"Ismi Familiyasi: {self.firstName} {self.lastName}")
        print(f"Oylik maoshi: {self.salary}")
        print()

    def toString(self):
        return f"ID: {self.id}, Ismi: {self.firstName}, Familiyasi: {self.lastName}, Oylik maoshi: {self.salary}"

natija = Employee(707011, "Aziz", "Jakbaraliyev", 100)
natija.det_info()
natija.set_salary(400)
natija.get_annualSalary()
natija.raise_Salary(1.2)
natija.det_info()
print(natija.toString())
