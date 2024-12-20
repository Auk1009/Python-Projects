string = 'Hello'
myit = iter(string)

for letters in string:
    print(next(myit))

mylamb = lambda a: a + 10

print(mylamb(2))