# Copyright 2024 Dev Sharma.
# Use of this source code is governed by The Unlicense
# which can be found in the LICENSE file.

from .weather_data import WeatherData


class WeatherData:
    def __init__(self: WeatherData, city: str, temperature: float, humidity: float, description: str):
        self.city = city
        self.temperature = temperature
        self.humidity = humidity
        self.description = description
