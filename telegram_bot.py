from aiogram.utils import executor
from data_for_the_bot import dp
from handlers import for_client, for_admin
from data_base import sqlite_db


async def show_launch_notification(_):
    print('Bot started!')
    sqlite_db.sql_start()

for_client.registration_handler_client(dp)
for_admin.registration_handlers_admin(dp)
for_admin.registration_callback_query_handler(dp)

executor.start_polling(dp, skip_updates=True, on_startup=show_launch_notification)

