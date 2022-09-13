import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher


bot_aiogram = Bot(token=os.getenv('TOKEN'))


dp = Dispatcher(bot_aiogram)
