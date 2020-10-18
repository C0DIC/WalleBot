from aiogram import types
from ..Bot import walle
from ...Utils.GetFirstWordOfText import getFirstWord
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.RU.Commands.ActionsList import actions_m, actions_f


async def actions_filter(msg: types.Message):
    action = getFirstWord(msg.text.lower())
    sndr = msg.from_user
    target = msg.reply_to_message.from_user

    if action in actions_m or action in actions_f:
        await msg.answer(action)
        await msg.answer(
            '[{}]({}) {} [{}]({}) \| 😱'.format(
                returnNoneReserved(sndr.first_name),
                sndr.url,
                returnNoneReserved(action),
                returnNoneReserved(target.first_name),
                target.url
            ),
            parse_mode = 'MarkdownV2'
        )