import random
from aiogram import types
from ..Bot import walle
from ..Strings.RU.Errors.PointTargetError import point_target
from ..Strings.RU.Commands.DuelGame import MainText, Win, DrawGame, GameKeyboard
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved



async def duel_command(msg: types.Message):
    try:
        sndr = msg.from_user
        target = msg.reply_to_message

        if target is None:
            await msg.reply(
                point_target,
                parse_mode = 'MarkdownV2'
            )
        else:
            await msg.reply(
                MainText.main_duel_text.format(
                    returnNoneReserved(target.from_user.first_name),
                    target.url,
                    returnNoneReserved(sndr.first_name),
                    sndr.url
                ),
                parse_mode = 'MarkdownV2',
                reply_markup = GameKeyboard.game_keyboard
            )
    except Exception as e:
        print(e)