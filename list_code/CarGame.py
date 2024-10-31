import os  
ColorList = []
url = '/Users/aryanuk/Documents/python/output1.txt'
def addColour(i):
    ColorList.append(i)
    with open(url, 'a') as textFile:
        print(textFile.write(i))
        print(textFile.write('\n'))
    print(ColorList)


def FindColour(x):
    for colour in ColorList:
        if colour == x:
            print(f"{x} is Found")
            break
        else:
            print(f"{x} is not Found")
    
    with open(url, 'r') as file:
        for line in file:
            print(line)
            if line.strip() == x:
                print(f"{x} is Found in database")
                break
            else:
                print(f"{x} is not Found in data base")

                



def delColour(z):
    for color in ColorList:
        if color == z:
            print(f"Yes, Color is found and can be deleted")
            ColorList.pop(z)
        else:
            print(f"Colour does not exist")

while(True):
    selector = int(input('press 1 to add colour, press 2 to delete color, press 3 to find the color: '))

    if selector == 1:
        addcol = input('Add the color: ')
        addColour(addcol)
        print(ColorList)
        print(f"{addcol} has been added")
    elif selector == 2:
        delcol = input('delete the color: ')
        delColour(delcol)
        print(ColorList)
        print(f"{delcol} has been deleted")
    else:
        find = input("find the your color: ")
        FindColour(find)

# url = '/Users/aryanuk/Documents/python/'
# with open(url+'output1.txt', 'r') as textFile:
#     # contents = textFile.read()
#     print(textFile.read())

