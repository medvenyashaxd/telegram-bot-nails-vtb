from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

button_price = KeyboardButton('💶 Прайс')
button_location = KeyboardButton('📍 Расположение')
button_see_works = KeyboardButton('👀 Посмотреть работы')

client_button = ReplyKeyboardMarkup(resize_keyboard=True).add(button_price).add(button_location).add(button_see_works)