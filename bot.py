import logging
import asyncio
from contextlib import suppress
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.utils.exceptions import (MessageToEditNotFound, MessageCantBeEdited, MessageCantBeDeleted,
                                      MessageToDeleteNotFound, Throttled)

import inline_keyboard
import messages
import config
from ban_words import lst_ban_words
logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.BOT_API_TOKEN)
dp = Dispatcher(bot, storage=MemoryStorage())

delay_flood = 10

async def anti_flood_command(*args, **kwargs):
    m = args[0]
    await delete_message(m)

@dp.message_handler(commands=['help'])
@dp.throttled(anti_flood_command, rate=delay_flood)
async def show_help(message: types.Message):
    await message.answer(text=messages.help())

@dp.message_handler(commands=['weather'])
@dp.throttled(anti_flood_command, rate=delay_flood)
async def show_weather(message: types.Message):
    await message.answer(text=messages.weather())

@dp.message_handler(content_types=["text"])
async def delete_ban_word(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    for i in lst_ban_words:
        if i in (message.text).lower():
            with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
                await message.delete()
            break

async def delete_message(message: types.Message, sleep_time: int = 0):
    await asyncio.sleep(sleep_time)
    with suppress(MessageCantBeDeleted, MessageToDeleteNotFound):
        await message.delete()


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
