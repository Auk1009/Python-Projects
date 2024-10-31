import tkinter as tk
import requests

def getWeather():
    try:
        apiKey = 'b62d99636369937d5de85404d8a8f7ca'
        baseURL = "http://api.openweathermap.org/data/2.5/weather"
        
        city = CityinputText.get()
        # unitResponse = input('Choose unit: c for Celsius or f for Fahrenheit:')
        unit = 'imperial'

        completeUrl = f"{baseURL}?q={city}&appid={apiKey}&units={unit}"
        print(completeUrl)
        response = requests.get(completeUrl)

        if response.status_code == 200:
            data = response.json()
            main = data['main']
            temp = main['temp']
            visibility = data['visibility']
            windSpeed = data['wind']['speed']

            label_3.config(text=f'The weather of {city} is:' )
            label_temp.config(text=f'Temperature: {temp} C')
            label_visibiliy.config(text=f"Visibility: {visibility}")
            label_windspeed.config(text=f"Wind speed: {windSpeed}")
        elif response.status_code == 404:
            label_3.config(text='City Not Found, please try again')
            label_temp.config(text='')
            label_visibiliy.config(text=f"")
            label_windspeed.config(text=f"")
        else:
            label_3.config(text='Please try again')
            label_temp.config(text='')
            label_visibiliy.config(text=f"")
            label_windspeed.config(text=f"")
    except Exception as e:
        label_3.config(text=f"Error: {str(e)}")

root = tk.Tk()

root.geometry("300x600")

root.title("Quick Weather")

label = tk.Label(root,text="Today's weather", padx=20, pady=10)
label.pack()

label2 = tk.Label(root,text='Which city do you what the weather of?', pady=10,  anchor='w')
label2.pack()

CityinputText = tk.Entry(root, justify='left')
CityinputText.pack()

button_result = tk.Button(root, text='Done', command=getWeather, pady=10)
button_result.pack()

label_3 = tk.Label(root,text='')
label_3.pack()

label_temp = tk.Label(root,text='')
label_temp.pack()

label_visibiliy = tk.Label(root,text='')
label_visibiliy.pack()

label_windspeed = tk.Label(root,text='')
label_windspeed.pack()


root.mainloop()




    