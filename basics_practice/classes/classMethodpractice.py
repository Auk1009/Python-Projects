class Movie:
    def __init__(self,title,rating):
        self.title = title
        self.rating = rating

    def change_rating(self,newrating):
        self.rating = newrating
        return newrating
    

movie1 = Movie('Don',4.5)

print(movie1.rating)

print(movie1.change_rating(3.5))
        
print(movie1.rating)