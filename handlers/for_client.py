from aiogram import types, Dispatcher
from data_for_the_bot import bot_aiogram


async def command_start(message: types.Message):
    try:
        await bot_aiogram.send_message(message.from_user.id,

'Здравствуй, {0.first_name}. Хочешь записаться на маникюр или педикюр? Чтобы узнать свободное время мастера,\
 напиши в личные сообщения https://t.me/medvenyashaxd или позвони по номеру +375336483246'.format(message.from_user))

        await bot_aiogram.send_message(message.from_user.id,
                                       'Узнай дополнительную информацию - жми на кнопки внизу чата ⬇')
    except:
        await message.delete()


def register_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
