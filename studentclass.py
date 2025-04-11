class student:
    
    def __init__(self,name:str,age:int,percentage:int,standard:int):
        self.name = name
        self.age = age
        self.percentage = percentage
        self.standard = standard
        
    def display(self):
        return(f"Name:{self.name} ,Age:{self.age} ,Percentage:{self.percentage}")
    
    def newper_and_newstd(self,new_percentage,new_std):
        self.percentage = new_percentage
        self.standard = new_std
        
student1 = student('Sudu',15,80,10)

print(student.display(student1))

newper = input(f'New percentage: ')
newstd = input('New Standard: ')

student.newper_and_newstd(student1,newper,newstd)

# print(student1.percentage)
print(student1.percentage)
print(student1.standard)
           		

	
            
            