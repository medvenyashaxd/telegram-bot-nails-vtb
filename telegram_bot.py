from aiogram.utils import executor
from data_for_the_bot import dp


async def show_launch_notification(_):
    print('Bot started!')


executor.start_polling(dp, skip_updates=True, on_startup=show_launch_notification)

