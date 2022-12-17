from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
import config

bot = Bot(config.token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()


backend_button = KeyboardButton("/Backend")
frontend_button = KeyboardButton("/Frontend")
uxui_button = KeyboardButton("/uxui")
android_button = KeyboardButton("/Android")
ios_button = KeyboardButton("/IOS")

buttons = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
buttons.add(backend_button)
buttons.add(frontend_button)
buttons.add(uxui_button)
buttons.add(uxui_button)
buttons.add(ios_button)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(f'''Добро пожаловать на IT-курсы GeekTech. Выберите свой курс:
    - Backend(кнопка "Backend")
    - Frontend(кнопка "Frontend")
    - uxui(кнопка "uxui)"
    - Android(кнопка "Android")
    - IOS(кнопка"IOS")''', reply_markup=buttons)

@dp.message_handler(commands=['Backend'])
async def back(message: types.Message):
    await message.answer("Backend — это внутренняя часть сайта и сервера и т.д", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=['Frontend'])
async def front(message: types.Message):
    await message.answer("Frontend — это внешняя часть сайта и сервера и т.д", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 5 месяц")

@dp.message_handler(commands=['uxui'])
async def uxui(message: types.Message):
    await message.answer("Uxui — это дизайн сайта.", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 3 месяц")

@dp.message_handler(commands=['Android'])
async def android(message: types.Message):
    await message.answer("Android — разработка андроид прогрмамм", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 7 месяц")


@dp.message_handler(commands=['IOS'])
async def ios(message: types.Message):
    await message.answer("Ios — разработка ios прогрмамм", reply_markup=buttons)
    await message.answer("Стоимость 10000 сом в месяц")
    await message.answer("Обучение: 12 месяц")


executor.start_polling(dp)
