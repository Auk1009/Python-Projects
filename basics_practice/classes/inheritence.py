class Shape:
    def __init__(self,measurement):
        self.measurement = measurement
        
class Circle(Shape):
    def __init__(self,measurement):
        super().__init__(measurement)
    @property
    def calculate_area(self):
        result = 3.14*self.measurement**2
        print(result)


class Rectangle(Shape):
    def __init__(self,length, breadth):
        self.length = length
        self.breadth = breadth
        
    @property
    def calculate_area(self):
        result = self.length * self.breadth
        print(result)


a = Circle(50)

a.calculate_area

b = Rectangle(10,5)

b.calculate_area