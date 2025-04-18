import requests
from ss import *

key2="71f274eb2cdb2dfadab3130d99ef0372"
api_address="http://api.openweathermap.org/date/2.5/weather?q=Kolhapur&appid="+ key2
json_data = requests.get(api_address).json()

def temp():
    temperature = round(json_data["main"][temp]-273, 1)
    return temperature

def des():
    description = json_data["weather"][0]["discription"]
    return description

print(temp())
print(des())