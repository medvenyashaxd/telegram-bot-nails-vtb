import os

from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

bot_aiogram = Bot(token=os.getenv('TOKEN'))

memory_storage = MemoryStorage()

dp = Dispatcher(bot_aiogram, storage=memory_storage)
