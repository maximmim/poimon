from aiogram import Bot, types
from aiogram.types import ReplyKeyboardRemove, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
import aiogram
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.utils.emoji import emojize

import re
import os
import random
from time import sleep
import time


import yt_download as yt
import config 


def random_id():
    return random.randint(0, 1000000)

bot = Bot(config.TOKEN)
URL = "https://painmo.herokuapp.com/"
dp = Dispatcher(bot)

b1 = KeyboardButton('Помощь')
b2 = KeyboardButton('Скачять')

kb_client = ReplyKeyboardMarkup()
kb_client.add(b1).add(b2)

   
@dp.message_handler(commands=['start'])
async def process_help_command(message: types.Message):
    await message.reply("Привіт!\n Я Паймон і допоможу завантажити відео з будь-якого сайту якщо потрібна допомога пиши /help")
    await message.delete()



@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply(config.STARTEXT)
    await message.reply("Надішліть мені посилання на відео \n і я допоможу завантажити його")
    await message.delete()
@dp.message_handler(content_types=['text'])
async def echo_download_message(message: types.Message):
    try:
        await message.reply("Побачила, починаю закачку...")    
        echo_download=yt.Downloader(message.text)   
        videonote = open(echo_download.download_video(), 'rb')
     
    except:
        await message.reply("На жаль, сталася помилка... Перевірте правильність посилання")
        print('Error :(')
        return
    await message.reply("Готово, видео зкачено на сервер.\nВідправляю...",)
    try:
        await bot.send_document(message.from_user.id, videonote)
    except:
        await bot.send_message(message.from_user.id, "На жаль, сталася помилка...")
    finally:
        videonote.close()





print("Оно живое !")
executor.start_polling(dp)