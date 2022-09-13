from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

button_price = KeyboardButton('💶 Прайс')
button_location = KeyboardButton('📍 Расположение')
button_see_works = KeyboardButton('👀 Посмотреть работы')


inline_button = InlineKeyboardMarkup(row_width=1)
inline_inst = InlineKeyboardButton(text='Instagram', url='https://www.instagram.com/val_ensya')


inline_button.add(inline_inst)
client_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_price).add(button_location).add(button_see_works)