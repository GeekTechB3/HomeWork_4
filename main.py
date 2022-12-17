from aiogram import Bot, Dispatcher, executor, types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from pytube import YouTube
import config

bot = Bot(config.token)
dp = Dispatcher(bot)

backend_button = KeyboardButton("/backend")
frontend_button = KeyboardButton("/frontend")
uxui_button = KeyboardButton("/uxui")
android_button = KeyboardButton("/android")
ios_button = KeyboardButton("/ios")

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons.add(backend_button)
buttons.add(frontend_button)
buttons.add(uxui_button)
buttons.add(android_button)
buttons.add(ios_button)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    await message.answer(f"""Здраствуйте, {message.from_user.full_name} """, reply_markup=buttons)

@dp.message_handler(commands=["start"])
async def start(message : types.Message):
    await message.answer(f"Здравствуйте, {message.from_user.full_name}. Добро пожаловать в Geektech, если хотите узнать по больше нажмите Помощь или напишите /help", reply_markup=buttons)


@dp.message_handler(commands=["backend"])
async def backend(message:types.Message):
    await message.answer("Backend — это разработка бизнес-логики продукта (сайта или веб-приложения). Бэкенд отвечает за взаимодействие пользователя с внутренними данными, которые потом отображает фронтенд. Попросту говоря, это то, что скрыто от глаз пользователя и происходит вне его браузера и компьютера.", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=["frontend"])
async def frontend(message:types.Message):
    await message.answer("Frontend — это создание пользовательского интерфейса на клиентской стороне веб‑сайта или приложения. Это всё, что видит пользователь, когда открывает веб-страницу, и с чем он взаимодействует: кнопки, баннеры и анимация.", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=["uxui"])
async def uxui(message:types.Message):
    await message.answer("Uxui — это проектирование удобных, понятных и эстетичных пользовательских интерфейсов. Чтобы разобраться, какие задачи решает специалист в этой сфере, нужно понять, что такое UX и UI. UX — user experience — переводится на русский язык как «пользовательский опыт».", reply_markup=buttons)
    await message.answer("Стоимость 11000 сом в месяц")
    await message.answer("Обучение: 5 месяц")


@dp.message_handler(commands=["android"])
async def android(message:types.Message):
    await message.answer("Android разработка — создает мобильные приложения на операционной системе Android. Андроид-программист использует языки Java, Kotlin, C++, иногда Javascript. В 2019 году Google объявил Kotlin официальным и предпочтительным языком для Android-разработки.", reply_markup=buttons)
    await message.answer("Стоимость 14000 сом в месяц")
    await message.answer("Обучение: 6 месяц")


@dp.message_handler(commands=["ios"])
async def ios(message:types.Message):
    await message.answer("IOS — разработчик создаёт приложения не только для iPhone, но и для iPad, Apple Watch и других гаджетов, входящих в экосистему. Он не только пишет код и работает над интерфейсом, но и занимается поддержкой приложения, адаптацией его под разные модели устройств, тестированием и исправлением багов.", reply_markup=buttons)
    await message.answer("Стоимость 14000 сом в месяц")
    await message.answer("Обучение: 5 месяц")
executor.start_polling(dp)    