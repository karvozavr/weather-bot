import os
import logging

from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineQuery, InlineQueryResultArticle, InputTextMessageContent

API_TOKEN = os.getenv('TELEGRAM_API_TOKEN') 
# PROXY_URL = os.getenv('TELEGRAM_PROXY_URL')
# PROXY_AUTH = os.getenv('TELEGRAM_PROXY_AUTH')

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def start(message: types.Message):
    await message.reply("Погода в вашем городе.", reply=False)

@dp.inline_handler()
async def inline_handler(query: InlineQuery):
    location = query.location
    result_id: str = f'{location.latitude}, {location.longitude}'
    item = InlineQueryResultArticle(
        id=result_id,
        title=f'Result {result_id!r}',
        input_message_content=InputTextMessageContent("Aaaaaaa"),
    )


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


