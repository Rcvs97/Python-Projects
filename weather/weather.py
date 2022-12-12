import tkinter as tk
import requests
import time

def getWeather(canvas):
    city = textField.get()
    api = "https://api.openweathermap.org/data/2.5/weather?q=" + city +"&APPID=0914777447c0ae5123ba565f50c6ddd3&units=imperial"


    json_data = requests.get(api).json()
    condition = json_data['weather'][0]['main']
    temp = int(json_data['main']['temp'])
    mintemp = int(json_data['main']['temp_min'])
    maxtemp = int(json_data['main']['temp_max'])
    pressure = json_data['main']['pressure']
    humidity =  json_data['main']['humidity']
    wind = json_data['wind']['speed']
    sunrise = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunrise'] - 10800))
    sunset = time.strftime("%I:%M:%S", time.gmtime(json_data['sys']['sunset'] - 10800))

    final_info = condition + "\n" + str(temp) + "°F"
    final_data = "\n" + "Max Temp: " + str(maxtemp) + "°F" + "\n" + "Min Temp: " + str(mintemp) + "°F" + "\n" + "Pressure: " + str(pressure) + "\n" + "Humidity: " + str(humidity) + "%" "\n" + "Wind Speed: " + str(wind) + "mph" "\n" + "Sun Rise: " + sunrise + "AM" "\n" + "Sun Set: " + sunset + "PM"

    label1.config(text = final_info)
    label2.config(text = final_data)

canvas = tk.Tk()
canvas.geometry("600x500")
canvas.title("Weather App")
f = ("poppins", 15, "bold")
t = ("poppins", 35, "bold")

textField = tk.Entry(canvas, justify='center', width = 20, font = t)
textField.pack(pady = 20)
textField.focus()
textField.bind('<Return>', getWeather)

label1 = tk.Label(canvas, font=t)
label1.pack()
label2 = tk.Label(canvas, font=f)
label2.pack()
canvas.mainloop()





