import sqlite3

from data_for_the_bot import bot_aiogram


# database connection
def sql_start():
    global base, cursor
    base = sqlite3.connect('valensiya_nails.db')
    cursor = base.cursor()
    if base:
        print('Data base connected!')

    base.execute('CREATE TABLE IF NOT EXISTS price(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


# adding data to the database
async def sql_add_data(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO price VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()


# reading data from database and sending this data to chat
async def sql_read(message):
    for data in cursor.execute('SELECT * FROM price').fetchall():
        await bot_aiogram.send_photo(message.from_user.id, data[0], f'{data[1]}\n{data[2]}\nСтоимость работы: {data[-1]}')


# select data to delete
async def sql_read_for_del():
    return cursor.execute('SELECT * FROM price').fetchall()


# deletes data
async def sql_run_delete(data):
    cursor.execute('DELETE FROM price WHERE name == ?', (data,))
    base.commit()
