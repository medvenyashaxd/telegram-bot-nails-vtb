from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

# adding buttons for admin in admin mode

button_load = KeyboardButton('Загрузить')
button_delete = KeyboardButton('Удалить')
button_cancel = KeyboardButton('Отмена')

buttons_admin = ReplyKeyboardMarkup(resize_keyboard=True).add(button_load, button_delete, button_cancel)
