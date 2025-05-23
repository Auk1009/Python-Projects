class Vehicle:
    count = 0
    def __init__(self, brand, model, color, type):
        self.brand = brand
        self.model = model
        self.color = color
        self.type = type
        Vehicle.count = Vehicle.count + 1

    def start(self):
        print(f'{self.brand} has started its engine')

    def show_info(self):
        print(f' Type: {self.type}\n Brand: {self.brand}\n Model: {self.model}\n Color: {self.color}\n')

    def __str__(self):
        return (f' Type: {self.type}\n Brand: {self.brand}\n Model: {self.model}\n Color: {self.color}\n')
    
    @classmethod
    def total_count(cls):
        return Vehicle.count



class Car(Vehicle):

    def __init__(self, brand, model, color, isElectric : bool):
        super().__init__(brand, model, color, type='car')
        self.isElectric = isElectric

    def show_info(self):
        super().show_info()
        print(f'Is it electric: {self.isElectric}')

    def start(self):
        if self.isElectric:
            print(f'{self.brand} has started its engine silently')
        else:
           super().start()

    def isEnvirnment_Friendly(vehicle_obj):
        if vehicle_obj.isElectric == True:
            print('This car is eco-friendly')
        else:
            print('This car is not eco-friendly')


class Scooter(Vehicle):

    def __init__(self, brand, model, color, isElectric):
        super().__init__(brand, model, color, type='Scooter')
        self.isElectric = isElectric

    def show_info(self):
        super().show_info()
        print(f'Is it electric: {self.isElectric}')

    def start(self):
        if self.isElectric:
            print(f'{self.brand} has started its engine silently')
        else:
           super().start()
        
    def isEnvirnment_Friendly(vehicle_obj):
        if vehicle_obj.isElectric == True:
            print('This scooter is eco-friendly')
        else:
            print('This scooter is not eco-friendly')
    


# Car objects
car1 = Car("Tesla", "Model 3", "Red", True)
car2 = Car("Toyota", "Camry", "Black", False)
car3 = Car("Hyundai", "Ioniq 5", "Silver", True)
car4 = Car('Hyundai', 'Creta Nline', 'Black', False)
# Scooter objects
scooter1 = Scooter("Ola", "S1 Pro", "Blue", True)
scooter2 = Scooter("Honda", "Activa", "White", False)
scooter3 = Scooter("Ather", "450X", "Blue", True)


car1.show_info()
car3.start()

scooter1.show_info()
scooter3.start()

# Polymorpishm

Garage1 = [car1,car4,scooter3]

for vehical in Garage1:
    Car.isEnvirnment_Friendly(vehical)

print(Vehicle.total_count())



class Garage1:
    def __init__(self,name):
        self.vehicles = []
        self.name = name

    def add_vehicle(self,obj:Vehicle):
        self.vehicles.append(obj)

    def count_list(self):
        print(len(self.vehicles))
        car = 0
        scooter = 0
        for vh in self.vehicles:
            if type(vh) == Car:
                car = car + 1
            elif type(vh) == Scooter:
                scooter = scooter +1 

            print(f'In {self.name} there is {car} cars and {scooter} scooter')
        

myGarage = Garage1('My Garage')

myGarage.add_vehicle(scooter1)

myGarage.add_vehicle(car1)

myGarage.add_vehicle(car2)

myGarage.add_vehicle(scooter2)

myGarage.count_list()






















# class Garage:

#     def __init__(self,name):
#         self.vehicles =[]
#         self.name = name


#     def addVehicle(self,vh:Vehicle):
#         self.vehicles.append(vh)

#     def countVehicles(self,name):
#         vehicleCounter = len(self.vehicles)
#         print(f"Vehicle count in garage {name} is {vehicleCounter}")
#         return vehicleCounter
    
#     def show(self):
#         for v in self.vehicles:
#             print(v)
    
#     def garageName(self):
#         return self.garageName


# myGarage  = Garage("Aryan")


# myGarage.addVehicle(car2)
# myGarage.addVehicle(car1)
# print(myGarage.vehicles)
# # myGarage.countVehicles("Aryan")

# # myGarage.show()
