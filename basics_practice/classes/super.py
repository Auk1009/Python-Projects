class Employee:
    def __init__(self):
        print('Constructure of Employee')

class Programmer(Employee):
    def __init__(self):
        print('Constructure of Programmer')

class Manager(Programmer,Employee):
    def __init__(self):
        super().__init__()
        print('Constructure of Manager')

o = Manager()