from aiogram import types

from loader import dp


# Echo bot
@dp.message_handler(state=None)
async def bot_echo(message: types.Message):

    await message.reply(f"Menga uzatilgan xabar jo'natsangiz\nUni ma'lumotlarini tashlab bera olaman.")
