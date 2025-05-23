class Class:
    def __init__(self,standard,section,no_of_students):
        self.standard = standard
        self.section = section
        self.no_of_students = no_of_students

    def __str__(self):
        return (f'Standard: {self.standard}, Section: {self.section}, Number of students per class: {self.no_of_students}')
    
    def add_student(self,number):
        new_no_of_students = self.no_of_students + number
        self.no_of_students = new_no_of_students
        return new_no_of_students
    
    def remove_student(self,number):
        new_no_of_students = self.no_of_students - number
        self.no_of_students = new_no_of_students
        return new_no_of_students

