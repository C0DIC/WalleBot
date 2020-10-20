import asyncio
from aiogram import types
from ...Utils.RemoveUnderlineSymbol import removeUnderline
from ...Utils.CheckForColon import checkColon
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ...Utils.CompareUsers import compareUsers
from ..Strings.RU.Commands.ActionsTexts.MainActionsText import main_act_text
from ..Strings.RU.Commands.ActionsTexts.UserIsTargetText import user_is_target_text
from ..Strings.RU.Errors.ActionMissingTargetError import MissingTargetError
from ..Strings.RU.Commands.ActionsTexts.SoloActionText import solo_act_text


async def actions_filter(msg: types.Message):
    try:
        if checkColon(msg.text):
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
                if ':' in msg.text.split()[0] and len(msg.text.split()[0]) > 1:
                    action = removeUnderline(msg.text.split()[0].replace(':', '').lower())
                    action_args = msg.text.lower().split()[1::]
                else:
                    action = removeUnderline(msg.text.split()[1].lower())
                    action_args = msg.text.lower().split()[2::]

                action_addition = ''

                for i in range(0, len(action_args)):
                    action_addition += ' ' + action_args[i]

                await msg.answer(
                    main_act_text.format(
                        returnNoneReserved(sndr.first_name),
                        sndr.url,
                        action,
                        returnNoneReserved(target.from_user.first_name),
                        target.from_user.url,
                        returnNoneReserved(action_addition)
                    ),
                    parse_mode = 'MarkdownV2'
                )
                await asyncio.sleep(2)
                await msg.delete()
        else:
            pass
    except Exception as e:
        print(e)