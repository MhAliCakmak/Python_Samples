class Employee:

    def __init__(self, name, surname, id, salary):
        self.name = name
        self.surname = surname
        self.id = id
        self.salary = salary

    def all_name(self):
        return f"{self.name} {self.surname}"

    def extras(self, extra):
        return self.salary * extra

    def __str__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        return self.salary + other.salary


class Boss(Employee):
    def __init__(self, name, surname, id, salary, worker=None):
        super().__init__(name, surname, id, salary)
        self.e_mail = self.name + self.surname + "@zygox.com"

        if worker == None:
            self.worker = 0
        else:
            self.worker = worker

    def worker_list(self):
        for i in self.worker:
            print(i.name)

    @property
    def e_posta(self):
        return self.name + self.surname + "@zygox.com"

    @property
    def full_name(self):
        return f"{self.name} {self.surname}"

    @full_name.setter
    def full_name(self, svalue):
        name, surname = svalue.split(" ")
        self.name = name
        self.surname = surname

    @full_name.deleter
    def full_name(self):
        self.name = None
        self.surname = None
        print("User Deleted ")


employee1 = Employee("mehmet", "Sali", 0, 3000)
employee2 = Employee("Cihan ", "Red", 1, 2589)
boss1 = Boss("Mehmet", "Ali", 3, 7800, [employee1, employee2])
boss1.name = "Fırat"
boss1.full_name = "Fırat Vandi"

print(employee1 + employee2)
print(boss1.worker_list())

print(boss1.name)

del boss1.full_name
