# Copyright 2024 Dev Sharma.
# Use of this source code is governed by The Unlicense
# which can be found in the LICENSE file.

class RepositoryFactory:
    def __init__(self, api_key):
        self.api_key = api_key

    def create_weather_repository(self):
        # !TODO: ExternalWeatherAPIAdapter(self.api_key)
        pass
