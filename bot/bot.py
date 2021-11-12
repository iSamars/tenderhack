from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton

import os

bot = Bot(token = os.environ.get("TELEGRAM_KEY"))

dp = Dispatcher(bot)
KeyBoard = ReplyKeyboardMarkup()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    catalog_bt = KeyboardButton('Каталог товаров')
    login_bt = KeyboardButton('Авторизоваться')
    KeyBoard = ReplyKeyboardMarkup(resize_keyboard=True).add(catalog_bt, login_bt)
    await message.reply("Вас приветсвует бот Портала Поставщиков", reply_markup=KeyBoard)

@dp.message_handler(lambda message: message.text == "Авторизоваться")
async def login_command(message: types.Message):
   await bot.send_message(message.from_user.id, "Введите логин")
   pass
   await bot.send_message(message.from_user.id, "Введите пароль")
   pass

def run_pooling():
    executor.start_polling(dp)