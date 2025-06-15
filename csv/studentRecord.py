import csv
record = []
with open('Student_Record.csv','r') as file:
    reader = csv.reader(file)
    for row in reader:
        record.append(row)

    
class StudentRecord:
    def __init__(self,name,clas,marks):
        self.name = name
        self.clas = clas 
        self.marks = marks

    def display(self):
        print(f"Student: {self.name}, Class: {self.clas}, Marks: {self.marks}")

student = StudentRecord(record[1][0],record[1][1],record[1][2])

student.display()
    

