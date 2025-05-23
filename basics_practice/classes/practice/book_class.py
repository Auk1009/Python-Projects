class Book:
    def __init__(self,title:str,author:str,pages:int):
        self.title = title
        self.author = author
        self.pages = pages

    def display(self):
        print(f'Title: {self.title}, Author: {self.author}, Pages: {self.pages}')

    

book1 = Book('Atomic Habits','James Clear',340)
