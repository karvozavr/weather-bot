import os
import logging

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN') 
# PROXY_URL = os.getenv('TELEGRAM_PROXY_URL')
# PROXY_AUTH = os.getenv('TELEGRAM_PROXY_AUTH')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Погода в вашем городе.", reply=False)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


