# import libraries
import mathstropy
import requests
import pygame

#------------------------------------------------------
# Weather API
URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = "19375602113c10e69b03a7ecc71e655f"
textinput = mathstropy.TextInput(initial_string="Toronto", font_size=30)  # change initial string depending on starting city
var = {}  # dictionary to store weather data displayed on app screen

# Make API Request
# Response [200] is good!
# Response [401] something went wrong, check your parameters

#------------------------------------------------------
# Week 8: start coding here!
def getWeather():
    global var
    pass