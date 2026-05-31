import requests

#variables
api_key="69f0baa029438f04ec42e756f8fd23c9"
city= input("Enter your city: ")
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

#function
response=requests.get(url)
if response.status_code == 200:
    print("fetching weather data from OpenWeather")
    data=response.json()
    print(data)
else:
    print("data not found")




