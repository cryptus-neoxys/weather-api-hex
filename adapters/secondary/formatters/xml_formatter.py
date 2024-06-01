# Copyright 2024 Dev Sharma.
# Use of this source code is governed by The Unlicense
# which can be found in the LICENSE file.

import dicttoxml
from ports import WeatherFormatter
from core.entities import WeatherData


class XMLWeatherDataFormatter(WeatherFormatter):
    def format(self, weather_data: WeatherData, format_flag: str) -> str:
        data = {
            'city': weather_data.city,
            'temperature': weather_data.temperature,
            'humidity': weather_data.humidity,
            'description': weather_data.description
        }
        return dicttoxml.dicttoxml(data).decode()
