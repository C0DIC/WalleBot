import asyncio
from aiogram import types

from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ...Utils.RemoveUnderlineSymbol import removeUnderline
from ...Utils.CheckForSpecialSym import checkSpecialSym
from ...Utils.CheckForSpecialSym import isTargetSym
from ...Utils.CheckForSpecialSym import isSndrSym
from ...Utils.CompareUsers import compareUsers

from ..Strings.RU.Commands.ActionsTexts.UserIsTargetText import user_is_target_text
from ..Strings.RU.Commands.ActionsTexts.MainActionsText import main_act_text
from ..Strings.RU.Commands.ActionsTexts.SoloActionText import solo_act_text


async def actions_filter(msg: types.Message):
    try:
        msg_text = msg.text

        if checkSpecialSym(msg_text):
            sndr = msg.from_user
            target = msg.reply_to_message

            if target is None:
                action = msg_text.replace('~', '')

                await msg.answer(
                    solo_act_text.format(
                        returnNoneReserved(sndr.first_name),
                        sndr.url,
                        action
                    ),
                    parse_mode = 'MarkdownV2'
                )
                await asyncio.sleep(1)
                await msg.delete()

            else:
                if compareUsers(sndr, target.from_user):
                    pass
                else:
                    action = returnNoneReserved(msg_text).replace('~', '')

                    if isSndrSym(action) is False and isTargetSym(action) is False:
                        action = removeUnderline(action)

                        await msg.answer(
                            main_act_text.format(
                                returnNoneReserved(sndr.first_name),
                                sndr.url,
                                action,
                                returnNoneReserved(target.from_user.first_name),
                                target.from_user.url
                            ),
                            parse_mode = 'MarkdownV2'
                        )
                        await asyncio.sleep(1)
                        await msg.delete()
                    else:
                        if isSndrSym(action):
                            act_sndr = f'[{returnNoneReserved(sndr.first_name)}]({sndr.url})'
                            action = action.replace('@', act_sndr)

                        if isTargetSym(action):
                            act_target = f'[{returnNoneReserved(target.from_user.first_name)}]({target.from_user.url})'
                            action = action.replace('_', act_target)

                        action = returnNoneReserved(action + ' | 💬')

                        await msg.answer(
                            action,
                            parse_mode = 'MarkdownV2'
                        )

                        await asyncio.sleep(1)
                        await msg.delete()
        else:
            pass
    except Exception as e:
        print(e)
