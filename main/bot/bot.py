import os
import django
import redis
from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from main.bot import keyboards as kb
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardRemove, \
    ReplyKeyboardMarkup, KeyboardButton, \
        InlineKeyboardMarkup, InlineKeyboardButton, ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher.filters.state import State, StatesGroup
from asgiref.sync import sync_to_async

# models
from tenderhack.wsgi import *
from main.models import *

conn = redis.Redis(host="localhost", decode_responses=True)
conn.hmset('main_menu', kb.main_menu)
conn.hmset('authorization_menu', kb.authorization_menu)

bot = Bot(token = "2122252291:AAFbYFCPJ6CQSc1C6JqzJyAzEZskpEbiOzk")#"2100248624:AAH1VI29il7JQXprwi-Gsdsiglo0tAWEah8")
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)

class Form(StatesGroup):
    serach_product = State()

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    KeyBoard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(conn.hgetall('main_menu')['catalog_bt']),
        KeyboardButton(conn.hgetall('main_menu')['login_bt'])
    )
    await message.reply("Вас приветсвует бот Портала Поставщиков", reply_markup=KeyBoard)

@dp.message_handler(lambda message: message.text == "Авторизоваться")
async def login_command(message: types.Message):
   previos_menu = "main_menu"
   KeyBoard = ReplyKeyboardMarkup(resize_keyboard=True).add(
        KeyboardButton(conn.hgetall('authorization_menu')['back_bt'])
   )
   await bot.send_message(message.from_user.id, "Введите логин", reply_markup=KeyBoard)
   await bot.send_message(message.from_user.id, "Введите пароль")

@dp.message_handler(lambda message: message.text == "Назад")
async def back(message: types.Message):
    if kb.previos_menu == "main_menu":
        KeyBoard = ReplyKeyboardMarkup(resize_keyboard=True).add(
            KeyboardButton(conn.hgetall('main_menu')['catalog_bt']),
            KeyboardButton(conn.hgetall('main_menu')['login_bt'])
        )
        await message.reply("Возврат в предедущие меню",reply_markup=KeyBoard)

@dp.message_handler(lambda message: message.text == "Поиск товаров")
async def serach_product(message: types.Message):
    await Form.serach_product.set()
    await message.reply("Введите товар для поиска")

@dp.message_handler(state='*', commands='cancel')
@dp.message_handler(Text(equals='отмена', ignore_case=True), state='*')
async def cancel_handler(message: types.Message, state: FSMContext):
    current_state = await state.get_state()
    if current_state is None:
        return

    await state.finish()
    await message.reply('ОК')

def _get_categories():
    return Category.objects.values("name")

def _get_stu():
    return STU.objects.values("name")

def _get_stu_by_category(category):
    return STU.objects.filter(category=Category.objects.filter(name=category).first()).values("name")

def _get_stu_by_filtr(filter):
    return STU.objects.filter(name=filter).values("name")    

@dp.message_handler(state=Form.serach_product)
async def process_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        bd = await sync_to_async(_get_categories)()
        print(bd)
        data['serach_product'] = message.text
        valuesList = []
        for bd_dict in bd:
            for key in bd_dict: 
                valuesList.append(bd_dict[key])
        i = 0
        inline_category_keyboard = InlineKeyboardMarkup()
        key_words = process.extractOne(data['serach_product'], valuesList)

        if key_words[1] > 97:
            coincidences = []
            bd = await sync_to_async(_get_stu_by_category)(key_words[0])
            for bd_dict in bd:
                for key in bd_dict: 
                    valuesList.append(bd_dict[key])
            print(valuesList)        
            for val in valuesList:
                if fuzz.partial_ratio(val, data['serach_product']) > 93:
                    coincidences.append(val)
            print(coincidences)        
            if len(coincidences) > 0:
                for coincidence in coincidences:
                    print(coincidence)
                    i+=1
                    inline_category_btn = InlineKeyboardButton(coincidence, callback_data=f'cat_{coincidence[0]}_{i}')
                    inline_category_keyboard.add(inline_category_btn)
                    if i == 5:
                        await message.reply("Подходящие товары", reply_markup=inline_category_keyboard)
                        return
            else:
                await message.reply("Товары не найдены, попробуйте еще раз")
                return
            return

        elif key_words[1] < 98:
            print(key_words[0])
            valuesList.clear
            stu_list = []
            stu_bd = await sync_to_async(_get_stu_by_filtr)(key_words[0])
            for stu_dict in stu_bd:
                for key in stu_dict: 
                    stu_list.append(stu_dict[key])
            #for value in stu_list:
            #    if fuzz.WRatio(key_words[0],value) > 98:
            #        key_words = value
            #        print(value)
            for stu in stu_list:
                i+=1
                inline_category_btn = InlineKeyboardButton(stu, callback_data=f'cat_{stu[0]}_{i}')
                inline_category_keyboard.add(inline_category_btn)
                if i == 5:
                    await message.reply("Подходящие товары", reply_markup=inline_category_keyboard)
                    back
            
        else:
            i = 0
            for category in process.extract(key_words[0],valuesList, limit=8): #получние категорий
                i+=1
                inline_category_btn = InlineKeyboardButton(category[0], callback_data=f'cat_{category[0]}')
                inline_category_keyboard.add(inline_category_btn)
                if i == 3:
                    await message.reply("Найдено несколько категорий", reply_markup=inline_category_keyboard)
                    break
        await state.finish()

@dp.callback_query_handler(lambda c: c.data.startswith('cat_'))
async def process_callback_button(callback_query: types.CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        await bot.answer_callback_query(callback_query.id)
        inline_category_keyboard = InlineKeyboardMarkup
        valuesList = []
        coincidences = []
        key_words = callback_query.data.replace('cat_','')
        print(key_words)
        bd = await sync_to_async(_get_stu_by_category)(key_words)
        for bd_dict in bd:
            for key in bd_dict: 
                valuesList.append(bd_dict[key])
        for val in valuesList:
            if fuzz.WRatio(val, data['serach_product']) > 93:
                coincidences.append(val)
        if len(coincidences) > 0:
            i = 0
            for coincidence in coincidences:
                i+=1
                inline_category_btn = InlineKeyboardButton(coincidence[0], callback_data=f'cat_{coincidence[0]}_{i}')
                inline_category_keyboard.add(inline_category_btn)
                if i == 5:
                    await bot.send_message(callback_query.from_user.id,"Подходящие товары", markup=inline_category_keyboard)
                    return
        else:
            i=0
            for value in valuesList:
                i+=1
                inline_category_btn = InlineKeyboardButton(value[0], callback_data=f'cat_{value[0]}_{i}')
                inline_category_keyboard.add(inline_category_btn)
                if i == 5:
                    await bot.send_message(callback_query.from_user.id,"Подходящие товары", markup=inline_category_keyboard)
                    return
    await state.finish()

def run_pooling():
    executor.start_polling(dp)
    # 2100248624:AAH1VI29il7JQXprwi-Gsdsiglo0tAWEah8