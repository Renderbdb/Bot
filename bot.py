import logging
import os
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# Код берет токен из Environment Variables на Render
API_TOKEN = os.getenv('BOT_TOKEN')

logging.basicConfig(level=logging.INFO)
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = InlineKeyboardMarkup(row_width=2)
    markup.add(InlineKeyboardButton("Кнопка 1", callback_data="b1"), 
               InlineKeyboardButton("Кнопка 2", callback_data="b2"))
    await message.answer("Привет! Вот твои кнопки:", reply_markup=markup)

@dp.callback_query_handler()
async def kb(callback: types.CallbackQuery):
    await callback.answer(f"Нажато: {callback.data}")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
