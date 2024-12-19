import sqlite3

con = sqlite3.connect('database.db')
cursor = con.cursor()

def initiate_db():

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            price INTEGER NOT NULL
        )
    ''')

    con.commit()


    query = '''
    CREATE INDEX IF NOT EXISTS idx_title ON Products(title)
    '''

    cursor.execute(query)
    con.commit()

def add_product():

    # Создаем список продуктов с их описаниями и ценами
    products = [
        {
            'name':'Лечебный сбор трав № 1',
            'description':'Лечебные травы горного Алтая для восстанавливания организма',
            'price':'100'
        },
        {
            'name':'Лечебный сбор трав № 2',
            'description':'Лечебные травы горного Алтая для восстанавливания организма',
            'price':'200'
        },
        {
            'name':'Лечебный сбор трав № 3',
            'description':'Лечебные травы горного Алтая для восстанавливания организма',
            'price':'300'
        },
        {
            'name':'Лечебный сбор трав № 4',
            'description':'Лечебные травы горного Алтая для восстанавливания организма',
            'price':'400'
        }
    ]

    for product in products:

        query = '''
        INSERT INTO Products
        (title, description, price)
        VALUES
        (?, ?, ?)
        '''

        cursor.execute(query, (product['name'], product['description'], product['price']))
        con.commit()


def get_all_products():
    import sqlite3

    con = sqlite3.connect('database.db')
    cursor = con.cursor()

    query = '''
    SELECT id, title, description, price, photo_path
    FROM Products
    ORDER BY title
    '''

    cursor.execute(query)
    products = cursor.fetchall()
    con.close()
    return products


#initiate_db()
#add_product()
#prod_list = get_all_products()
#print(prod_list)

con.close()
