import random
class Cars:
    def __init__(self, brand: str, model: str, price: int, color:str, inGarage: bool)-> None:
        self.brand = brand
        self.model = model
        self.price = price
        self.color = color
        self.inGarage = inGarage

    def __str__(self)-> str:
        return(f'Brand: {self.brand}, Model: {self.model}, Price:{self.price}, Color: {self.color}')

    def viewCars(self):
        if self.inGarage == True:
            print(f'{self.brand} {self.model} is in Garage')
        else:
            print(f'{self.brand} {self.model} not in Garage')


    
balence = 200000000
def viewBalence():
    print(balence)

def buyCar(whichCar : str) -> Cars:
    for car in carlist:
        if car.brand.lower() == whichCar:
            print(f"Found car {whichCar}")
            if car.inGarage == False:
                print(car)
                return car
            else:
                print(f'You already own {car.brand}')
                
    

def sellcar(cartoBeSold:str) -> Cars:
    for car in carlist:
        if car.brand.lower() == cartoBeSold:
            print(f"Found car {cartoBeSold}")
            if car.inGarage == True:
                print(car)
                return car
            else:
                 print(f'You do not own {car.brand} ') 

def drive():
    print('driving....')
    accident = random.randint(1,10)
    accident_price = random.randint(100000,200000)
    print('Safely completed to drive')
    # 1 drive point is 10,000 rupees
    if accident >= 7:
        print('You have had a car crash ')
        print(f'You will have to pay {accident_price}')
    global drive_points
    drive_points = 5
    print(f'You have recieved {drive_points} drive points')
    return drive_points

                
        

volvo:Cars = Cars(brand='volvo', model='5x',price=500000,color='Black',inGarage=True)
ferrari = Cars(brand='Ferrari', model='La Ferrari', price=12000000,color='Red',inGarage=False)
Tesla = Cars(brand='Tesla', model='Model S', price=8000000, color='White', inGarage=True)
bmw = Cars(brand='BMW', model='X5', price=6000000, color='Blue', inGarage=False)
audi = Cars(brand='Audi', model='Q7', price=7000000, color='Gray', inGarage=True)
mb = Cars(brand='Mercedes-Benz', model='G-Class', price=9000000, color='Black', inGarage=True)
porsche = Cars(brand='Porsche', model='Cayenne', price=8500000, color='Red', inGarage=False)
ford = Cars(brand='Ford', model='Mustang', price=5500000, color='Yellow', inGarage=True)
chev = Cars(brand='Chevrolet', model='Camaro', price=5200000, color='Orange', inGarage=False)
lambo = Cars(brand='Lamborghini', model='Aventador', price=12000000, color='Green', inGarage=True)
bugatti = Cars(brand='Bugatti', model='Chiron', price=20000000, color='Blue', inGarage=False)
toyata = Cars(brand='Toyota', model='Supra', price=3000000, color='Red', inGarage=True)
carlist = [volvo,ferrari,Tesla,bmw,audi,mb,porsche,ford,chev,lambo,bugatti,toyata]
def view_cars():
    for cars in carlist:
        if cars.inGarage == True:  
            cars.viewCars()
            print()

while True:
    userInput = input('do you what to buy(1), sell(2), view bank balence(3), view cars(4),drive(5) ?')

    if userInput == '1':

        whichCar = input('which car do you what: ')

        car:Cars = buyCar(whichCar)
        if car!= None:
            pay = input(f'please pay the price, type pay')
            car.inGarage = True
            if pay == 'pay'.lower():
                balence = balence - car.price
                print(balence)


    elif userInput == '2':

        sellCar = input('which car do you what to sell?')
        car:Cars = sellcar(sellCar)
        if car != None:
            sell = input('if you what is sell it type sell')
            car.inGarage = False
            if sell == 'sell'.lower():
                balence += car.price
                print(balence)

    elif userInput == '3':
        viewBalence()
    
    elif userInput == "4":
        view_cars()

    elif userInput == "5":
        drive()



    

