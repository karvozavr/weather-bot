import logging
import os

import aiohttp.client
from aiogram.types import Location
import urllib


WEATHER_SERVICE_API_KEY = os.getenv('WEATHER_SERVICE_API_KEY')


class WeatherServiceException(BaseException):
    pass


class WeatherInfo:

    def __init__(self, temperature, status, is_kelvin=True):
        self.temperature = kelvin_to_celsius(
            temperature) if is_kelvin else temperature
        self.status = status


async def get_weather_for_city(city_name: str) -> WeatherInfo:
    return await make_weather_service_query(get_city_query_url(city_name))


async def get_weather_for_location(location: Location) -> WeatherInfo:
    return await make_weather_service_query(get_location_query_url(location))


def get_city_query_url(city_name: str):
    return f'http://api.openweathermap.org/data/2.5/weather?q={urllib.parse.quote(city_name)}&appid={WEATHER_SERVICE_API_KEY}&lang=ru'


def get_location_query_url(location: Location):
    return f'http://api.openweathermap.org/data/2.5/weather?lat={location.latitude}&lon={location.longitude}&appid={WEATHER_SERVICE_API_KEY}&lang=ru'


async def make_weather_service_query(url: str) -> WeatherInfo:
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as resp:
            if resp.status == 200:
                return get_weather_from_response(await resp.json())

    raise WeatherServiceException()


def get_weather_from_response(json):
    return WeatherInfo(json['main']['temp'], json['weather'][0]['description'])


def kelvin_to_celsius(degrees):
    KELVIN_0 = 273.15
    return degrees - KELVIN_0
