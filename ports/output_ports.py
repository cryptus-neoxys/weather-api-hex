from abc import ABC, abstractmethod
from core.entities import WeatherData


class WeatherDataFormatter(ABC):
    @abstractmethod
    def format(self, weather_data: WeatherData, format_flag: str) -> str:
        pass
