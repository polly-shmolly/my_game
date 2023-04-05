from aiogram import Bot, Dispatcher, types
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from aiogram.utils import executor
from asgiref.sync import sync_to_async

bot = Bot(token='6174127131:AAHACugqtwYOiLFQ-p4IAYjvUAUc0FIZQWE')
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start(message: types.Message):
    mess = f"Hello, {message.from_user.first_name}"
    await message.answer(mess, reply_markup=keyboard)


@sync_to_async()
def get_data():
    with open('high_score.txt', 'r') as f:
        data = f.readline()
    return data


@dp.message_handler(lambda message: message.text == 'High Score')
async def certain_message(msg: types.Message):
    data = await get_data()
    name = data.split(' ')[0]
    coin = data.split(' ')[1]

    msg_to_answer = f'Username: {name}\nGet coins: {coin}'
    await bot.send_message(msg.from_user.id, msg_to_answer)


button = KeyboardButton('High Score')
keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=False)
keyboard.add(button)


executor.start_polling(dp)



