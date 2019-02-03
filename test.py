
import json
import requests
from requests.auth import HTTPBasicAuth

class RestApi:

    def __init__ (self, url):
        self.url = url
        print("Object created")

    def get(self , query_params, username, password, headers):

        response = requests.get(self.url , auth=HTTPBasicAuth(username, password) , headers = headers, params= query_params)

        data = response.json()

        return data

restapi = RestApi("https://samples.openweathermap.org/data/2.5/weather")

# url = "https://samples.openweathermap.org/data/2.5/weather"
params_1 = {
    "lat" : "10",
    "lon" : "139",
    "appid" : "6907d289e10d714a6e88b30761fae22"
      }

username = ""
password = ""
headers = {}

output = restapi.get( params_1, username , password , headers)
print(output)

