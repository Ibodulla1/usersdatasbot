from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    text = "Men rasm,video,audio,ovozli xabar va matnlarning ma'lumotini tashlab bera olaman."
    
    await message.answer(text)
