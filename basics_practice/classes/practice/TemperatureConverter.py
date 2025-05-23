class Temperature:
    def __init__(self,celsius:float):
        self.celsius = celsius

    def convertToFahrenheit(self):
        fahrenheit = (self.celsius * 9/5) + 32
        print(f'Fahrenheit: {fahrenheit}')

    def convertToKelvin(self):
        kelvin = self.celsius + 273.15
        print(f'Kelvin: {kelvin}')



temp1 = Temperature(36)

temp1.convertToFahrenheit()
temp1.convertToKelvin()
    
