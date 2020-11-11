import asyncio
from aiogram import types
from ...Utils.RemoveUnderlineSymbol import removeUnderline
from ...Utils.CheckForSpecialSym import checkSpecialSym
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ...Utils.CompareUsers import compareUsers
from ...Utils.ReadAction import readFirstAction
from ...Utils.ReadBeforeAction import readBeforeAction
from ..Strings.RU.Commands.ActionsTexts.MainActionsText import main_act_text
from ..Strings.RU.Commands.ActionsTexts.UserIsTargetText import user_is_target_text
from ..Strings.RU.Commands.ActionsTexts.SoloActionText import solo_act_text


async def actions_filter(msg: types.Message):
    try:
        if checkSpecialSym(msg.text):
            sndr = msg.from_user
            target = msg.reply_to_message

            if target is None:
                action = returnNoneReserved(msg.text[1::].lower())

                await msg.answer(
                    solo_act_text.format(
                        returnNoneReserved(sndr.first_name),
                        sndr.url,
                        action
                    ),
                    parse_mode = 'MarkdownV2'
                )
                await asyncio.sleep(2)
                await msg.delete()
            else:
                before_ = readBeforeAction(msg.text)
                after_ = readFirstAction(msg.text)
                after__ = msg.text.replace(after_, '').replace(before_, '')

                await msg.answer(
                    main_act_text.format(
                        returnNoneReserved(before_.replace('[', '')),
                        returnNoneReserved(sndr.first_name),
                        sndr.url,
                        returnNoneReserved(after_.replace('(', '')),
                        returnNoneReserved(target.from_user.first_name),
                        target.from_user.url,
                        returnNoneReserved(after__)
                    ),
                    parse_mode = 'MarkdownV2'
                )
                await asyncio.sleep(2)
                await msg.delete()
        else:
            pass
    except Exception as e:
        print(e)
