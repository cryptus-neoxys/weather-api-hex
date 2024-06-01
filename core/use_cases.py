# Copyright 2024 Dev Sharma.
# Use of this source code is governed by The Unlicense
# which can be found in the LICENSE file.

class FetchWeatherUseCase:
    def __init__(self, weather_repository, formatter):
        self.weather_repository = weather_repository
        self.formatter = formatter

    def execute(self, city, format_flag):
        weather_data = self.weather_repository.get_weather_data(city)
        return self.formatter.format(weather_data, format_flag)
