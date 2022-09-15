from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram import types, Dispatcher
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from data_base.sqlite_db import sql_add_data, sql_read_for_del, sql_run_delete
from data_for_the_bot import bot_aiogram
from buttons.buttons_for_admin import buttons_admin

ID = None


class FSMAdmin(StatesGroup):
    photo = State()
    name = State()
    description = State()
    price = State()


async def command_change_price(message: types.Message):
    global ID
    ID = message.from_user.id
    await bot_aiogram.send_message(message.from_user.id, 'Готов к указаниям.', reply_markup=buttons_admin)
    await message.delete()


async def loading_command(message: types.Message):
    if message.from_user.id == ID:
        await FSMAdmin.photo.set()
        await message.reply('Загрузи фото:')

    else:
        await message.delete()
        await bot_aiogram.send_message(message.from_user.id, 'Сначала нужно получить права администратора!')


async def cancel_command(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        current_state = await state.get_state()
        if current_state is None:
            return

        else:
            await state.finish()
            await message.reply('Отмена произведена')


async def load_photo(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == ID:
            data['photo'] = message.photo[0].file_id
            await FSMAdmin.next()
            await message.reply('Введи название работы/процедуры:')


async def load_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        if message.from_user.id == ID:
            data['name'] = message.text
            await FSMAdmin.next()
            await message.reply('Введи описание:')


async def load_description(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['description'] = message.text
            await FSMAdmin.next()
            await message.reply('Введи цену: ')


async def load_price(message: types.Message, state: FSMContext):
    if message.from_user.id == ID:
        async with state.proxy() as data:
            data['price'] = message.text

        await bot_aiogram.send_message(message.from_user.id, 'Данные внесены')

        await sql_add_data(state)
        await state.finish()


async def run_del_price(callback: types.CallbackQuery):
    await sql_run_delete(callback.data.replace('del ', ''))
    await callback.answer(text=f'{callback.data.replace("del ", "")} удалена.', show_alert=True)


async def delete_price(message: types.Message):
    if message.from_user.id == ID:
        read = await sql_read_for_del()
        for data in read:
            await bot_aiogram.send_photo(message.from_user.id, data[0], f'{data[1]}\n{data[2]}\nСтоимость работы '
                                                                        f'{data[-1]}')

            await bot_aiogram.send_message(message.from_user.id, text='⬆', reply_markup=InlineKeyboardMarkup(). \
            add(InlineKeyboardButton(f'Удалить {data[1]}', callback_data=f'del {data[1]}')))


def registration_handlers_admin(dp: Dispatcher):
    dp.register_message_handler(loading_command, lambda message: 'Загрузить' in message.text, state=None)
    dp.register_message_handler(cancel_command, lambda message: 'Отмена' in message.text, state='*')
    dp.register_message_handler(load_photo, content_types=['photo'], state=FSMAdmin.photo)
    dp.register_message_handler(load_name, state=FSMAdmin.name)
    dp.register_message_handler(load_description, state=FSMAdmin.description)
    dp.register_message_handler(load_price, state=FSMAdmin.price)
    dp.register_message_handler(command_change_price, commands=['admin'], is_chat_admin=True)
    dp.register_message_handler(delete_price, lambda message: 'Удалить' in message.text)


def registration_callback_query_handler(dp: Dispatcher):
    dp.register_callback_query_handler(run_del_price, lambda x: x.data and x.data.startswith('del '))

