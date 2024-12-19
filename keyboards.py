from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buttom_1 = KeyboardButton(text='Стоимость')
buttom_2 = KeyboardButton(text='О нас')
start_kb = ReplyKeyboardMarkup([[buttom_1, buttom_2]], resize_keyboard=True)

catalog_kb = InlineKeyboardMarkup()
buttom_1 = InlineKeyboardButton(text='Средняя Игра', callback_data='medium')
buttom_2 = InlineKeyboardButton(text='Большая Игра', callback_data='big')
buttom_3 = InlineKeyboardButton(text='Очень большая игра', callback_data='mega')
buttom_4 = InlineKeyboardButton(text='Другие предложения', callback_data='other')
catalog_kb.add(buttom_1)
catalog_kb.add(buttom_2)
catalog_kb.add(buttom_3)
catalog_kb.add(buttom_4)

buy_kb = InlineKeyboardMarkup()
buttom_5 = InlineKeyboardButton(text='Купить', url="https://ya.ru/")
buttom_6 = InlineKeyboardButton(text='Назад', callback_data='back_to_catalog')
buy_kb.add(buttom_5)
buy_kb.add(buttom_6)

admin_panel = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Пользователи', callback_data='users')],
        [InlineKeyboardButton(text='Статистика', callback_data='stat')],
        [
         InlineKeyboardButton(text='Блокировка', callback_data='block'),
         InlineKeyboardButton(text='Разблокировка', callback_data='unblock')
        ]
    ]
)

