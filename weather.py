import tkinter as tk
from tkinter import messagebox
import requests
import matplotlib.pyplot as plt

# Function to get weather data from OpenWeatherMap
def get_weather(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = base_url + "q=" + city_name + "&appid=" + api_key + "&units=metric"
    response = requests.get(complete_url)
    data = response.json()
    
    if data["cod"] != "404":
        weather_info = data["main"]
        weather_desc = data["weather"][0]["description"]
        temp = weather_info['temp']
        humidity = weather_info['humidity']
        wind_speed = data["wind"]["speed"]
        
        result = {
            "temperature": temp,
            "description": weather_desc,
            "humidity": humidity,
            "wind_speed": wind_speed
        }
        return result
    else:
        return None

# Function to display weather information in the GUI
def display_weather():
    city_name = city_entry.get()
    api_key = "your_openweather_api_key"  # Replace with your OpenWeatherMap API key
    
    weather_data = get_weather(city_name, api_key)
    
    if weather_data:
        result_label.config(
            text=f"Temperature: {weather_data['temperature']}°C\n"
                 f"Weather: {weather_data['description']}\n"
                 f"Humidity: {weather_data['humidity']}%\n"
                 f"Wind Speed: {weather_data['wind_speed']} m/s"
        )
        # Optionally, you could call visualize_weather() here with more data
    else:
        messagebox.showerror("Error", "City Not Found")

# Optional: Function to visualize temperature trends using matplotlib
def visualize_weather(temperatures, days):
    plt.plot(days, temperatures, marker='o')
    plt.title('Temperature Trend')
    plt.xlabel('Days')
    plt.ylabel('Temperature (°C)')
    plt.show()

# Tkinter GUI setup
root = tk.Tk()
root.title("Real-Time Weather Dashboard")

# GUI Elements
city_label = tk.Label(root, text="Enter City Name:")
city_label.pack()

city_entry = tk.Entry(root)
city_entry.pack()

get_weather_button = tk.Button(root, text="Get Weather", command=display_weather)
get_weather_button.pack()

result_label = tk.Label(root, text="")
result_label.pack()

# Example visualization trigger (optional)
# visualize_weather([21, 22, 20, 19, 23, 24, 22], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun'])

root.mainloop()
