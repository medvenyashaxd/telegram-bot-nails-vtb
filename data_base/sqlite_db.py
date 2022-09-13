import sqlite3


def sql_start():
    global base, cursor
    base = sqlite3.connect('valensiya_nails.db')
    cursor = base.cursor()
    if base:
        print('Data base connected!')

    base.execute('CREATE TABLE IF NOT EXISTS price(img TEXT, name TEXT PRIMARY KEY, description TEXT, price TEXT)')
    base.commit()


async def sql_add_data(state):
    async with state.proxy() as data:
        cursor.execute('INSERT INTO price VALUES (?, ?, ?, ?)', tuple(data.values()))
        base.commit()
