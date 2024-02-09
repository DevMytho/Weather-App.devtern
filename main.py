import tkinter as tk
import tk_tools
import requests
import json
from datetime import datetime
import os
import dotenv


Api = os.getenv("API_KEY")

root = tk.Tk()
root.geometry("1200x600")
root.resizable(0,0)

root.title('Python Weather App')

#-------------------

city_value = StringVar()


def time_format_for_location(utc_with_tz):
    local_time = datetime.utcfromtimestamp(utc_with_tz)
    return local_time.time()




def showWeather():
    api_key = Api
    city_name=city_value.get()
    weather_url = 'http://api.openweathermap.org/data/2.5/weather?q=' + city_name + '&appid='+api_key
    response = requests.get(weather_url)
    weather_info = response.json()
    tfield.delete("1.0", "end")













root.mainloop()
