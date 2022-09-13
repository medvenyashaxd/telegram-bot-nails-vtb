from aiogram.utils import executor
from data_for_the_bot import dp
from handlers import for_client, for_admin


async def show_launch_notification(_):
    print('Bot started!')

for_client.registration_handler_client(dp)
for_admin.registration_handlers_admin(dp)

executor.start_polling(dp, skip_updates=True, on_startup=show_launch_notification)

