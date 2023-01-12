from aiogram import types

from loader import dp

@dp.message_handler(content_types='photo')
@dp.message_handler(content_types='video')
@dp.message_handler(content_types='audio')
@dp.message_handler(content_types='voice')
@dp.message_handler(is_forwarded=True)
async def forwarded_example(messag:types.Message):
    try:
        data = f"""
Nickname: [ {messag.forward_from.full_name} ]
ID: <code>{messag.forward_from.id}</code>
Username: {messag.forward_from.mention}
"""
    except:
        data = f"Bu xabarning ma'lumotlarini olib bo'lmadi ❌\n"
    await messag.reply(data)

 # <code>Text</code>