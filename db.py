import sqlite3
import pandas as pd

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
        users_list = cursor.fetchall()
        message = ''

        print(users_list)

        for user in users_list:
            message += f"{user[0]} @{user[1]} @{user[2]} @{user[3]}\n"

        print(message)


def show_stat():
    query = '''
    SELECT COUNT(id)
    FROM users
    '''
    count_users = cursor.execute(query).fetchone()
    return count_users[0]


def add_to_block(input_id):
    query = '''
    UPDATE users
    SET block = ?
    WHERE id = ?
    '''
    cursor.execute(query, (1, input_id))
    con.commit()


def remove_block(input_id):
    query = '''
    UPDATE users
    SET block = ?
    WHERE id = ?
    '''
    cursor.execute(query, (0, input_id))
    con.commit()


def check_block(input_id):
    query = '''
    SELECT block
    FROM users
    WHERE id = ?
    '''
    check_block = cursor.execute(query, (input_id,)).fetchone()
    return check_block[0]


def select_user_frame():
    query = '''
    SELECT id, username, first_name, block
    FROM users
    ORDER BY username
    '''
    df = pd.read_sql_query(query, con)
    i = 1
    print(df.iloc[i].username, df.iloc[i].first_name, df.iloc[i].block)
    print(df.iloc[i].username)
    print(df.iloc[i].first_name)
    print(df.iloc[i].block)


#initiate_db()
#add_user('admin', 'admin', 0)
#dd_user('sbzhuk', 'sbzhuk', 0)
select_user()
#select_user_frame()

con.close()