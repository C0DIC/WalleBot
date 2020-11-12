import asyncio
from aiogram import types
from ...Utils.RemoveUnderlineSymbol import removeUnderline
from ...Utils.CheckForSpecialSym import checkSpecialSym
from ...Utils.CheckForSpecialSym import checkForSndrSyms
from ...Utils.CheckForSpecialSym import checkForTargetSyms
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
                msg_text = returnNoneReserved(msg.text.replace('~', ''))

                if checkForSndrSyms(msg_text):
                    msg_sndr = f'[{returnNoneReserved(sndr.first_name)}]({sndr.url})'
                    msg_text = msg_text.replace('@s', msg_sndr)

                if checkForTargetSyms(msg_text):
                    msg_target = f'[{returnNoneReserved(target.from_user.first_name)}]({target.from_user.url})'
                    msg_text = msg_text.replace('@y', msg_target)

                msg_action = msg_text + '\| 💬'

                await msg.answer(
                    msg_action,
                    parse_mode = 'MarkdownV2'
                )
                await asyncio.sleep(2)
                await msg.delete()
        else:
            pass
    except Exception as e:
        print(e)
