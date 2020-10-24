from aiogram import types
from ..Bot import walle

async def command(msg: types.Message):
    target = msg.forward_from
    await msg.reply("Name: {}\nId: {}\n".format(
        target.first_name,
        target.id,
    ))