class Rectangle:
    def __init__(self,length:float,Breadth:float):
        self.length = length
        self.Breadth = Breadth

    def calculate_Area(self):
        print(f"Area: {self.length*self.Breadth}")

    
    def calculate_Perimeter(self):
        print(f'Perimeter: {2*(self.length+self.Breadth)}')



rect1 = Rectangle(12,8)

rect1.calculate_Area()

rect1.calculate_Perimeter()