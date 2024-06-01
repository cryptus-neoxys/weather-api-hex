# Copyright 2024 Dev Sharma.
# Use of this source code is governed by The Unlicense
# which can be found in the LICENSE file.

from adapters.secondary.formatters.json_formatter import JSONWeatherDataFormatter
from adapters.secondary.formatters.xml_formatter import XMLWeatherDataFormatter


class FormatterFactory:
    def create_formatter(self, format_flag):
        if format_flag.lower() == 'json':
            return JSONWeatherDataFormatter()
        elif format_flag.lower() == 'xml':
            return XMLWeatherDataFormatter()
        else:
            raise ValueError('Unsupported format flag')
