from aiogram import Bot,Dispatcher,executor,types
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import KeyboardButton,ReplyKeyboardMarkup
from aiogram.dispatcher import FSMContext
import config

bot = Bot(token=config.token)
dp = Dispatcher(bot, storage=MemoryStorage())
storage = MemoryStorage()

backend_button = KeyboardButton("/Backend")
frontend_button = KeyboardButton("/Frontend")
uxui_button = KeyboardButton("/UXUI")
android_button = KeyboardButton("/Android")
ios_button = KeyboardButton("/IOS")

buttons = ReplyKeyboardMarkup(resize_keyboard=True).add(backend_button,frontend_button,uxui_button,android_button,ios_button)

@dp.message_handler(commands=["start"])
async def start(message : types.Message):
    await message.answer(f"""Здравствуйте, {message.from_user.full_name}.
Вас беспокоит школа программирования GeekTech.
            О нас:
Курсы IT-профессий GeekTech были основаны в 2018-ом году в Бишкеке с целью дать возможность каждому человеку, даже без опыта в технологиях, гарантированно освоить IT-профессию.
Основатели GeekTech - Айдар Бакиров и Нургазы Сулайманов
Чтобы узнать про направления нажмите /help""")

@dp.message_handler(commands=["help"])
async def help(message : types.Message):
    await message.reply("""Если вас интересует Веб-разработка могу предложить /Frontend и /Backend.
Если вас интересует разработка приложений могу предложить /Android и /IOS
Если вы считате себя творческой личностью то вам сюда /UXUI""", reply_markup=buttons)

@dp.message_handler(commands=["Backend"])
async def backend(message:types.Message):
    await message.answer("""Как понятно из названия Backend — это внутренняя часть сайта и сервера. 
Если говорить в целом, это программно-аппаратный комплекс, который позволяет сайту и серверу корректно работать.
Стоимость 10000 сом в месяц
Обучение длится 5 месяцев """)

@dp.message_handler(commands=["Frontend"])
async def frontend(message:types.Message):
    await message.answer("""Frontend — это разработка пользовательских функций и интерфейса. 
К ним относится всё, что пользователи видят на сайте или в приложении, и с чем можно взаимодействовать: картинки, выпадающие списки, меню, анимация, карточки товаров, кнопки, чекбоксы, интерактивные элементы.
Стоимость 10000 сом в месяц
Обучение длится 5 месяцев """)

@dp.message_handler(commands=["UXUI"])
async def uxui(message:types.Message):
    await message.answer("""UX/UI дизайн — это проектирование любых пользовательских интерфейсов в которых удобство использования так же важно как и внешний вид.
Стоимость 10000 сом в месяц
Обучение длится 3 месяцев """)

@dp.message_handler(commands=["Android"])
async def android(message:types.Message):
    await message.answer("""Android  —  самая популярная операционная система и платформа для приложений, насчитывающая больше двух миллиардов активных пользователей. 
На ней работают совершенно разные устройства, от «интернета вещей» и умных часов до телевизоров, ноутбуков и автомобилей, но чаще всего Android используют на смартфонах и планшетах.
Стоимость 10000 сом в месяц
Обучение длится 7 месяцев """)

@dp.message_handler(commands=["IOS"])
async def ios(message:types.Message):
    await message.answer("""iOS — операционная система, разработанная компанией Apple для своих портативных устройств.
В отличие от других мобильных операционных систем (например Android), может устанавливаться только на фирменных продуктах Apple.
Стоимость 10000 сом в месяц
Обучение длится 7 месяцев """)

executor.start_polling(dp, timeout=1000000)