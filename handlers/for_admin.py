from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from data_base.sqlite_db import sql_add_data
from data_for_the_bot import bot_aiogram

ID = None


async def command_change_price(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot_aiogram.send_message(message.from_user.id, 'Давай поменяем прайс', reply_markup=buttons_admin)
    await message.delete()


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def loading_command(message: types.Message):
    await FSMAdmin.photo.set()
    await message.reply('Загрузи фото:')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['photo'] = message.photo[0].file_id
        await FSMAdmin.next()
        await message.reply('Введи название работы/процедуры:')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи описание:')


async def load_description(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['description'] = message.text
        await FSMAdmin.next()
        await message.reply('Введи цену:')


async def load_price(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['price'] = (message.text + ' BYN')

    await bot_aiogram.send_message(message.from_user.id, 'Данные внесены')

    await sql_add_data(state)
    await state.finish()


def registration_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(loading_command, commands=['upload'], state=None)
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(command_change_price, commands=['admin'])
