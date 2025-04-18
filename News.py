#API(application programming interface):Help us to communicate between two different program
import requests
from ss import *     # I made a file named "ss" which has my secret api keys"

key="260a9597c2fa424d91fea80e28ff3e05"
api_address="http://newsapi.org/v2/top-headlines?country=us&apikey ="+ key
json_data = requests.get(api_address).json()

ar=[]
def news():
    if "articles" in json_data:
    #     for i in range(min(3, len(json_data["articles"]))):
    #         ar.append("Number "+ str(i+1) + " , " + json_data["articles"][i]["title"]+".")
    # return ar

         for i in range(3):
          ar.append("Number "+ str(i+1) + json_data["articles"][i]["title"]+".")
    return ar

