class Calculator:
    def __init__(self,number):
        self.number = number
    
    def findingsquare(self)-> int:
        square = self.number*self.number
        print(square)
    
    def findingcube(self):
        cube = self.number*self.number*self.number
        print(cube)
    
    def findingsquareroot(self):
        root = self.number**1/2
        print(root)
    
num1 = Calculator(4)

num1.findingcube()
num1.findingsquare()
num1.findingsquareroot()