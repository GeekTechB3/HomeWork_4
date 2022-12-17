from aiogram import Bot, Dispatcher, executor, types
from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup

import config
import logging



bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()
logging.basicConfig(level=logging.INFO)


backend_button = KeyboardButton("/backend")
frontend_button = KeyboardButton("/frontend")
uxui_button = KeyboardButton("/uxui")
android_button = KeyboardButton("/android")
ios_button = KeyboardButton("/ios")
program_button = KeyboardButton("/op")

developer_button = KeyboardButton("/developer")

help_buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
help_buttons.add("Направление:")
help_buttons.add("/backend")
help_buttons.add("/frontend")
help_buttons.add("/uxui")
help_buttons.add("/android")
help_buttons.add("/ios")
help_buttons.add("/op")
help_buttons.add("/разработчик")



buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(
    backend_button,frontend_button,uxui_button
).add(developer_button).row(
    android_button,ios_button,program_button)


@dp.message_handler(commands=['start', 'go'])
async def start(message : types.Message):
    await message.answer(f"Здраствуйте {message.from_user.full_name}!\nДобро пожаловать в Geektech!", reply_markup=help_buttons)

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

@dp.message_handler(commands=["разработчик"])
async def developer(message: types.Message):
    await message.answer("Меня создал Backend разработчик\n\nВот информация о нем -->>\nФ.И.О:  Nurbekow Aibala \nНация: Кыргыз🇰🇬\nГод рождание: 03.09.2005\nПол: Мужской\nПрофессия: Программист, Backend - разработчик\nАдресс: Кыргызстан/Ош\n\n Контакты -->>>\n\nTelegram: @aitmamatow\nInstagram: @nurbekow.7\n WhatsApp: +996-700-62-32-15\nТел.номер: +996-700-62-32-15",reply_markup=help_buttons)

executor.start_polling(dp,timeout=1000000000000000000000000)