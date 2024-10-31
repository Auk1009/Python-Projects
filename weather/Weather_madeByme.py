import requests

apiKey = "123"
baseUrl = "http://api.openweathermap.org/data/2.5/weather"

city = input('Which city weather do you want to see?   ')
unitResponse = input("a").upper() 
unit = "metric" if unitResponse == "C" else "imperial"

complete_url  = f"{baseUrl}?q={city}&appid={apiKey}&units={unit}"

response = requests.get(complete_url)
if response.status_code == 200:
    data = response.json()
    main = data['main']
    temp = main["temp"]
    windSpeed = data['wind']['speed']
    weather_description = data["weather"][0]["description"]
    visibility = data['visibility']

    print(f"Temperature: {temp}°C")
    print(f'Wind speed {windSpeed}')
    print(f"Description: {weather_description}")
    print(f"Visibility{visibility}")
else:
    print("Some thing went wrong")

if response.status_code == 404:
    data = response.json()
    print(data['message'])