import requests
import json
from datetime import datetime


class GetWeather():
    """Class of manipulate with weather"""

    def __init__(self, city: str = 'Moscow', file_name: str = 'Output.txt',
                 api_key: str = "bf0ab41056c6bdbcbb660f087c137e48",
                 base_url: str = "http://api.openweathermap.org/data/2.5/weather?"):
        self.city = city
        self.api_key = api_key
        self.base_url = base_url
        self.complete_url = base_url + "appid=" + api_key + "&q=" + self.city
        self.file_name = file_name

    # Function of getting weather
    def give_weather(self) -> str:
        response = requests.get(self.complete_url)  # Take info from API like GET response
        ans = response.json()  # Convertion in json format
        if str(response) == '<Response [200]>':  # Verifying a successful request
            self.output_message = f'''{self.city}_{datetime.now().replace(microsecond=0)}_{ans['weather'][0]['description']}'''
            print(self.output_message,end='\n\n')
            return self.output_message
        else:
            print(f'Error for {self.city} town')
            return f'Error for {self.city} town'


class DublicateInTxt():
    """Class of manipulate with output.txt
        self.output_message and self.file_name are inherited from the GetWeather class"""

    def __init__(self):
        pass

    def give_info(self) -> None:
        file = open(self.file_name,'a')
        print(self.output_message, file=file)
        pass


class UserClass(GetWeather, DublicateInTxt):
    """User class that inherits all methods from the parent"""
    pass


file = f'{input("Give a name file for save info about city: ")}.txt'    # Input file name for save info


while True:
    city = input("Input city's name for check weather: ")           # Input city for checking weather
    app = UserClass(city, file)                                     # Initialization work class
    app.give_weather()                                              # Get weather in terminal
    app.give_info()  # Save info in output file
    if input("Enough? (Y or N): ").capitalize() == 'N':
        break

