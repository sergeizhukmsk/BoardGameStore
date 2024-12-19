import logging

from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.types import Message
import asyncio

from admin import *
from db import *

from config import *
from keyboards import *
import texts

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())


@dp.message_handler(lambda message: message.text == 'Информация')
async def inform(message):
    await message.answer('Программа рассчета нормы калорий, исходя из вашего пола, возраста, роста и веса.')


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.answer(f'Добро пожаловать, уважаемый {message.from_user.username}\n' + texts.start,
                         reply_markup=start_kb)


# message.answer_photo
# message.answer_video
# message.answer_file


@dp.message_handler(lambda message: message.text == 'О нас')
async def price(message: types.Message):
    with open('./image/nerpa.png', 'rb') as img:
        await message.answer_photo(img, texts.about, reply_markup=start_kb)

    # with open('./video/siren.mp4', 'rb') as vid:
    #     await message.answer_video(vid, texts.about, reply_markup=start_kb)


@dp.message_handler(lambda message: message.text == 'Стоимость')
async def info(message: types.Message):
    await message.answer('Что Вас интересует?', reply_markup=catalog_kb)


@dp.callback_query_handler(text='medium')
async def buy_m(call: types.CallbackQuery):
    await call.message.answer(texts.Mgame, reply_markup=buy_kb)


@dp.callback_query_handler(text='big')
async def buy_l(call: types.CallbackQuery):
    await call.message.answer(texts.Lgame, reply_markup=buy_kb)


@dp.callback_query_handler(text='mega')
async def buy_xl(call: types.CallbackQuery):
    await call.message.answer(texts.XLgame, reply_markup=buy_kb)


@dp.callback_query_handler(text='other')
async def buy_other(call: types.CallbackQuery):
    await call.message.answer(texts.other, reply_markup=buy_kb)


@dp.callback_query_handler(text='back_to_catalog')
async def back(call: types.CallbackQuery):
    await call.message.answer('Что Вас интересует?', reply_markup=catalog_kb)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
