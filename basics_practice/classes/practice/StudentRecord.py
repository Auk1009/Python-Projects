class Student:
    noofStudents = 0
    def __init__(self,name:str,marks:float):
        self.__name = name
        self.__marks = marks
        Student.noofStudents += 1

    def getgrades(self):
        if self.__marks >= 90:
            return'A Grade'
        elif self.__marks >= 75 and self.__marks< 90:
            return'B'
        elif self.__marks >= 60 and self.__marks < 75:
            return'C'
        else:
            return'D'

    def displayStudentInfo(self):
        print(f'Student name: {self.__name}')
        print(f'Marks: {self.__marks}')
        print(f"Grade: {self.getgrades()}")



john = Student('John',80)
aryan = Student('Aryan',100)
aryan.getgrades()
aryan.displayStudentInfo()
print(aryan.noofStudents)