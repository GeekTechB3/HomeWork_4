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

help_button = KeyboardButton("/help")
backend_button = KeyboardButton("/backend")
frontend_button = KeyboardButton("/frontend")
uxui_button = KeyboardButton("/uxui")
android_button = KeyboardButton("/android")
ios_button = KeyboardButton("/ios")
program_button = KeyboardButton("/op")

developer_button = KeyboardButton("/developer")


help_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_buttons.add(help_button)
help_buttons.add(developer_button)

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    backend_button,frontend_button,uxui_button
).add(developer_button).row(
    android_button,ios_button,program_button)



@dp.message_handler(commands=["start"])
async def start(message : types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}. Добро пожаловать в Geektech, если хотите узнать по больше нажмите Помощь или напишите /help", reply_markup=help_buttons)

@dp.message_handler(commands=["help"])
async def help(message : types.Message):
    await message.answer(f"Обо мне->>>\nЯ телеграм помощник академии Geektech.\nЯ помогу вам с выбором курсов програмирование: \n\nЕсли хотите узнать что такое програмирование нажмите на /op:\nКстати вот наши курсы -->>>\n\nBackend разработка  - Если хотите узнать по больше нажмите на кнопку /backend.\nFrontend разработка - Если хотите узнать по больше нажмите на кнопку /frontend.\nUxui разработка- Если хотите узнать по больше нажмите на кнопку /uxui.\nAndroid разработка - Если хотите узнать по большенажмите на кнопку /android\nIos разработка - Если хотите узнать по большенажмите на кнопку /ios\nЕсли хотите узнать о моем создателе @erk1nbaev нажмите /developer", reply_markup=buttons)

@dp.message_handler(commands=["backend"])
async def backend(message:types.Message):
    await message.answer("Backend — это разработка бизнес-логики продукта (сайта или веб-приложения). Бэкенд отвечает за взаимодействие пользователя с внутренними данными, которые потом отображает фронтенд. Попросту говоря, это то, что скрыто от глаз пользователя и происходит вне его браузера и компьютера.", reply_markup=help_buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=["frontend"])
async def frontend(message:types.Message):
    await message.answer("Frontend — это создание пользовательского интерфейса на клиентской стороне веб‑сайта или приложения. Это всё, что видит пользователь, когда открывает веб-страницу, и с чем он взаимодействует: кнопки, баннеры и анимация.", reply_markup=help_buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=["uxui"])
async def uxui(message:types.Message):
    await message.answer("Uxui — это проектирование удобных, понятных и эстетичных пользовательских интерфейсов. Чтобы разобраться, какие задачи решает специалист в этой сфере, нужно понять, что такое UX и UI. UX — user experience — переводится на русский язык как «пользовательский опыт».", reply_markup=help_buttons)
    await message.answer("Стоимость 11000 сом в месяц")
    await message.answer("Обучение: 5 месяц")


@dp.message_handler(commands=["android"])
async def android(message:types.Message):
    await message.answer("Android разработка — создает мобильные приложения на операционной системе Android. Андроид-программист использует языки Java, Kotlin, C++, иногда Javascript. В 2019 году Google объявил Kotlin официальным и предпочтительным языком для Android-разработки.", reply_markup=help_buttons)
    await message.answer("Стоимость 14000 сом в месяц")
    await message.answer("Обучение: 6 месяц")


@dp.message_handler(commands=["ios"])
async def ios(message:types.Message):
    await message.answer("IOS — разработчик создаёт приложения не только для iPhone, но и для iPad, Apple Watch и других гаджетов, входящих в экосистему. Он не только пишет код и работает над интерфейсом, но и занимается поддержкой приложения, адаптацией его под разные модели устройств, тестированием и исправлением багов.", reply_markup=help_buttons)
    await message.answer("Стоимость 14000 сом в месяц")
    await message.answer("Обучение: 5 месяц")


@dp.message_handler(commands=["op"])
async def op(message:types.Message):
    await message.answer("Програмирование — процесс создания компьютерных программ.По выражению одного из основателей языков программирования Никлауса Вирта «Программы = алгоритмы + структуры данных»\nПрограммирование основывается на использовании языков программирования, на которых записываются исходные тексты программ.", reply_markup=help_buttons)
    await message.answer("Стоимость 12000 сом в месяц")
    await message.answer("Обучение: 1 месяц")

@dp.message_handler(commands=["developer"])
async def developer(message: types.Message):
    await message.answer("Меня создал Backend разработчик\n\nВот информация о нем -->>\nФ.И.О:  Erkinbaev Nurbolot Ilyazbekovich\nСвет: Черный \nНация: Кыргыз🇰🇬\nГод рождание: 27.11.2005\nПол: Мужской\nПрофессия: Программист, Backend - разработчик\nАдресс: Кыргызстан/Ош\n\n Контакты -->>>\n\nTelegram: @erk1nbaev\nInstagram: @erk1nbaew\n WhatsApp: +996-558-00-03-50\nТел.номер: +996-558-000-350",reply_markup=help_buttons)

executor.start_polling(dp,timeout=1000000000000000000000000)
