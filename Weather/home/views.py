from django.shortcuts import render
from .utils import get_weather_data

def weather(request):
    # Specify the location (coordinates or city name)
    location = 'Resistencia, AR'  # Replace with your desired location

    # Call the get_weather_data function with the location
    weather_data = get_weather_data(location)

    # Pass the weather_data to the template
    context = {'weather_data': weather_data}
    return render(request, 'weather.html', context)
