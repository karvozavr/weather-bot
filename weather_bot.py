import os
import logging

import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

from bot_messages import get_message
from weather_service import WeatherServiceException, WeatherInfo, get_weather_for_city, get_weather_for_location

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN')
PROXY_URL = os.getenv('TELEGRAM_PROXY_URL')
PROXY_AUTH = os.getenv('TELEGRAM_PROXY_AUTH')

logging.basicConfig(level=logging.DEBUG)

bot = Bot(token=API_TOKEN, proxy=PROXY_URL, proxy_auth=PROXY_AUTH)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Я умею показывать погоду в вашем городе, упомяните меня в сообщении @whatshouldiweartodaybot и введите название города.", reply=False)


@dp.message_handler(content_types=['text'])
async def get_weather_in_city(message: types.Message):
    try:
        weather: WeatherInfo = await get_weather_for_location(message.text)
    except WeatherServiceException:
        await message.reply(get_message('weather_for_location_retrieval_failed'))
        return
    await message.reply(get_message('weather_in_city_message').format(message.text, ))


@dp.message_handler()
async def default_response(message: types.Message):
    await message.reply(get_message('general_failure'))


@dp.message_handler(content_types=['location'])
async def get_weather_in_location(message: types.Message):
    if message.location:
        try:
            weather = await get_weather_for_location(message.location)
        except WeatherServiceException:
            await message.reply(get_message('weather_for_location_retrieval_failed'))
            return

        await message.reply(f'В указанной локации {str(weather)}.')
            
    await message.reply(get_message('weather_for_location_retrieval_failed'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

