from aiogram import types, Bot
from aiogram.dispatcher import Dispatcher, FSMContext
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from pathlib import Path
import requests

from db import BotDB
BotDB = BotDB('info.db')

bot = Bot(token='5528898419:AAFmtD9SgxHExDnJ7U4mVaSqD7Xhzg96ess')
dp = Dispatcher(bot, storage=MemoryStorage())

@dp.message_handler(commands = "start")
async def start(message: types.Message):
    if(not BotDB.user_exists(message.from_user.id)):
        BotDB.add_user(message.from_user.id)
    await message.bot.send_message(message.from_user.id, "Приветствую!")


@dp.message_handler(content_types=['text'])
async def join_msg(message):
    BotDB.add_msg(message.from_user.id, message.text)

@dp.message_handler(content_types=['photo', 'video', 'document'])
async def add_photo(message):
    fi = message.photo[0].file_id
    BotDB.add_id_file(message.from_user.id, fi)
    TOKEN = '5528898419:AAFmtD9SgxHExDnJ7U4mVaSqD7Xhzg96ess'
    requests.post(f'https://api.telegram.org/bot{TOKEN}/sendPhoto?chat_id=628072647&photo={fi}')



if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)