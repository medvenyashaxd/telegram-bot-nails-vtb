from aiogram import types, Dispatcher

from buttons.buttons_for_client import client_button
from data_for_the_bot import bot_aiogram


async def command_start(message: types.Message):
    try:
        await bot_aiogram.send_message(message.from_user.id,

'Здравствуй, {0.first_name}. Хочешь записаться на маникюр или педикюр? Чтобы узнать свободное время мастера,\
 напиши в личные сообщения https://t.me/medvenyashaxd или позвони по номеру +375336483246'.format(message.from_user),
                                       reply_markup=client_button)

        await bot_aiogram.send_message(message.from_user.id,
                                       'Узнай дополнительную информацию - жми на кнопки внизу чата ⬇')
    except:
        await message.delete()


async def send_location(message: types.Message):
    await message.reply('г. Витебск, ул. Калинина 18, салон красоты "Калинка"')
    await bot_aiogram.send_message(message.from_user.id, 'Посмотреть на карте:')
    await bot_aiogram.send_location(chat_id=message.from_user.id, latitude=55.186894, longitude=30.201958)


async def send_instagram(message: types.Message):
    await message.reply(f'Посмотреть работы в instagram:\nhttps://www.instagram.com/val_ensya/')


def registration_handler_client(dp: Dispatcher):
    dp.register_message_handler(command_start, commands=['start', 'help'])
    dp.register_message_handler(send_location, lambda message: '📍 Расположение' in message.text)
    dp.register_message_handler(send_instagram, lambda message: '👀 Посмотреть работы' in message.text)
