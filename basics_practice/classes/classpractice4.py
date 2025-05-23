class Circle:
    def __init__(self,radius):
        self.radius = radius
    
    def calculate_area(self):
        result = 3.14*self.radius**2
        print(result)

a = Circle(5)

a.calculate_area()