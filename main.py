from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

TOKEN = '1650077573:AAHfZMCUxCyMdBE42gpK9JPRcRVD0O2k_gQ'

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['Start'])
async def process_start_command(message: types.Message):
    await message.reply("Привет!\nЭто программа составления дежурств МООД.\nОсновные команд\n/Current - текущий график\n/Next - график на следующий месяц\n /Yes - прошу поставить на эти даты\n/No - прошу не ставить на эти даты \nВсе пожелания учитываются, но не являются обязательными")


@dp.message_handler(commands=['Current'])
async def process_help_command(message: types.Message):
    await message.reply("Здесь будет расписание на текущий месяц")

@dp.message_handler(commands=['Next'])
async def process_help_command(message: types.Message):
    await message.reply("Здесь будет расписание на следующий месяц")

@dp.message_handler(commands=['Yes'])
async def process_help_command(message: types.Message):
    await message.reply("Напишите через запятую дни, когда хотите дежурить\nПример - 1,5,10")

@dp.message_handler(commands=['No'])
async def process_help_command(message: types.Message):
    await message.reply("Напишите через запятую или тире дни, когда НЕ хотите дежурить\nПример - 1,3,5-10")


@dp.message_handler()
async def echo_message(msg: types.Message):
    await bot.send_message(msg.from_user.id, msg.text)


if __name__ == '__main__':
    executor.start_polling(dp)
