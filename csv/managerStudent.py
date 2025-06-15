import csv
class Student_manager:
    def __init__(self,records:list):
        self.csvfile = 'managerStudent.csv'
        self.records = records

    def addStudent(self,name:str,Rn:int,marks:int,clas:int,):
        self.records.append(name)
        self.records.append(Rn)
        self.records.append(marks)
        self.records.append(clas)
        print(self.records)
        print('saved in list')
        file = open(self.csvfile,'a')
        writer = csv.writer(file)
        writer.writerow(self.records)
        file.close()
        print('saved in csv')
        self.records.clear()


    def rnSearch(self,input):
        file = open(self.csvfile,'r')
        reader = csv.reader(file)
        self.records = list(reader)
        file.close()
        for stu in self.records:

            if stu[1] == input:
                print('Yes this RN exists')
                print(f'The student: {stu[1]} Roll number: {stu[0]}, Marks: {stu[2]}, Class {stu[3]}')
                break
            
       


    def display(self):
        file = open(self.csvfile,'r')
        reader = csv.reader(file)
        self.records = list(reader)
        file.close()
        print(self.records)

    def calcMarksAve(self):
        file = open(self.csvfile,'r')
        reader = csv.reader(file)
        self.records = list(reader)
        file.close()
        self.records.remove(['Name', 'RollNumber', 'Marks', 'Class'])
        score = 0
        score2 = 0
        for student in self.records:
            con = int(student[2])
            score = score + con
            score2 = score2 + 1
            # print(student[2])
            
        # print(score)
        average = score/score2
        print(f"The average marks are: {round(average,1)}")
        
running = True
while running:
    userinput = input("Add student(1), Roll number search(2), Display no of student(3), Average of student marks (4), exit(5) ")

    manager1 = Student_manager(records=[])
    if userinput == '1':
        name1 = input('Name: ')
        rn = input('Roll number: ')
        mark = input('marks: ')
        clas1 = input('Class: ')
        manager1.addStudent(name1,rn,mark,clas1)
    elif userinput == '2':
        rn_input = input('Find roll number: ')
        manager1.rnSearch(rn_input)
    elif userinput == '3':
        manager1.display()
    elif userinput == '4':
        manager1.calcMarksAve()
    elif userinput == '5':
        running = False
    else:
        print('Wrong input')






