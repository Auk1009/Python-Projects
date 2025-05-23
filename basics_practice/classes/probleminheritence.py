class Animal:
    def __init__(self):
        pass

class Pet(Animal):
    def __init__(self):
        super().__init__()

class Dog(Pet):
    def __init__(self):
        super().__init__()
        
    @staticmethod
    def bark():
        print("BARK!!!")


snoppy = Dog()

snoppy.bark()