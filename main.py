"""
This is a echo bot.
It echoes any incoming text messages.
"""

import logging
import SeleniumAPI

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '1415135417:AAGYUz4Txr18KpFLZHrsatD_QaCdU1LHB9k'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm EchoBot!\nPowered by aiogram.")



@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)
    text = message.text
    translation, origin = SeleniumAPI.translate(text, "ru")
    if origin == "JAPANESE":
        print(translation)
        await message.reply(translation)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)