import json
from ports.output_ports import WeatherFormatter
from core.entities import WeatherData


class JSONWeatherDataFormatter(WeatherFormatter):
    def format(self, weather_data: WeatherData, format_flag: str) -> str:
        data = {
            'city': weather_data.city,
            'temperature': weather_data.temperature,
            'humidity': weather_data.humidity,
            'description': weather_data.description
        }
        return json.dumps(data)
