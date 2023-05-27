import requests

def get_weather_data(location):
    api_key = 'ca0747bcf1b5283aa95ba2f07a2d184f'  # Replace with your actual API key
    base_url = 'http://api.openweathermap.org/data/2.5/weather'
    
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'
    }
    
    response = requests.get(base_url, params=params)
    
    if response.status_code == 200:
        data = response.json()
        
        temperature = data['main']['temp']
        description = data['weather'][0]['description']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        weather_data = {
            'temperature': temperature,
            'description': description,
            'humidity': humidity,
            'wind_speed': wind_speed
        }
        
        return weather_data
    
    return None

def format_temperature(temperature):
    celsius = round(float(temperature), 2)
    temperature_string = f"{celsius} °C"
    return temperature_string

def format_wind_speed(wind_speed):
    km_per_hour = round(float(wind_speed), 2)
    wind_speed_string = f"{km_per_hour} km/h"
    return wind_speed_string
