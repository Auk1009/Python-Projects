class Employee:
    a = 5
    @classmethod
    def show(cls):
        print(f'the class value of a is {cls.a}')


o = Employee()
o.a = 67
o.show()

