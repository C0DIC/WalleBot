from aiogram import types
from ..Bot import walle


async def mute_command(msg: types.Message):
    await msg.reply("Test: ok.")