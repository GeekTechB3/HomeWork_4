from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

import config
import logging
import os

bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)

help_button =KeyboardButton("/help")
android_button = KeyboardButton("/android")
backend_button = KeyboardButton("/backend")
frontend_button = KeyboardButton("/frontend")
uxui_button = KeyboardButton("/uxui")
ios_button = KeyboardButton("/ios")

help_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_buttons.add(help_button)

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    backend_button,frontend_button,uxui_button)

@dp.message_handler(commands=["start"])
async def start(message : types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}. Добро пожаловать в Geektech, если хотите узнать по больше нажмите Помощь или напишите /help", reply_markup=help_buttons)

@dp.message_handler(commands=["help"])
async def help(message : types.Message):
    await message.answer(f"Чем я могу помочь вам", reply_markup=buttons)

@dp.message_handler(commands=["backend"])
async def backend(message:types.Message):
    await message.answer("Backend — это разработка бизнес-логики продукта (сайта или веб-приложения). Бэкенд отвечает за взаимодействие пользователя с внутренними данными, которые потом отображает фронтенд. Попросту говоря, это то, что скрыто от глаз пользователя и происходит вне его браузера и компьютера.", reply_markup=help_buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=["android"])
async def android(message:types.Message):
    await message.answer("Android - это разработка мбильных приложений")
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 7 месяц")

@dp.message_handler(commands=["frontend"])
async def android(message:types.Message):
    await message.answer("Frontend - Это разработа сайтов")
    await message.answer("Стоимость - 10000 сом в месяц")
    await message.answer("Обучение: 5 месяцев")

@dp.message_handler(commands=["uxui"])
async def uxui(message:types.Message):
    await message.answer("uxui - Это дизайн разработка")
    await message.answer("Стоимость - 10000 сом в мецяц")
    await message.answer("Обучение: 3 месяца")

@dp.message_handler(commands=["ios"])
async def ios(message:types.Message):
    await message.answer("ios - это разработка приложений для ios")
    await message.answer("Стоимость - 10000 сом в мецяц")
    await message.answer("Обучение: 7 месяцев")

executor.start_polling(dp,timeout=1000000000000000000000000)