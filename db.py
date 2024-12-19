import sqlite3

con = sqlite3.connect('database.db')
cursor = con.cursor()


def initiate_db():

    query = '''
    CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    first_name TEXT NOT NULL,
    block INTEGER DEFAULT 0)
    '''

    cursor.execute(query)
    con.commit()

    query = '''
    CREATE INDEX IF NOT EXISTS idx_username ON users(username)
    '''

    cursor.execute(query)
    con.commit()


def add_user(username, first_name, block):

    query_select = '''
    SELECT * FROM Users
    WHERE username = ?
    '''

    check_user = cursor.execute(query_select, (username,))

    if check_user.fetchone() is None:
        query_insert = '''
        INSERT INTO users
        (username, first_name, block)
        VALUES
        (?, ?, ?)
        '''

        cursor.execute(query_insert, (username, first_name, block))
        con.commit()


def select_user():

    query = '''
    SELECT id, username, first_name, block
    FROM users
    ORDER BY username
    '''

    check_user = cursor.execute(query)

    if check_user.fetchone() is not None:
        cursor.execute(query)
        print(cursor.fetchall())


#initiate_db()
#add_user('admin', 'admin', 0)
#dd_user('sbzhuk', 'sbzhuk', 0)
select_user()

con.close()