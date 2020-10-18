from aiogram import types
from ..Bot import walle
from ...Utils.GetFirstWordOfText import getFirstWord
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ...Utils.removeUnderlineSymbol import removeUnderline
from ..Strings.RU.Commands.ActionsList import actions_m, actions_f, actions


async def actions_filter(msg: types.Message):
    try:
        action = removeUnderline(getFirstWord(msg.text.lower()))
        sndr = msg.from_user
        
        try:
            action_args = await msg.get_args().split(' ')[1::]
        except AttributeError:
            pass

        for i in action_args:
            action_addition += ' ' + action_args[i]


        if action in actions:
            target = msg.reply_to_message.from_user

            if action in actions[0]:
                await msg.answer(
                '[{}]({}) *хрюкнул\(\-а\) на* [{}]({})*{}* \| 🐽'.format(returnNoneReserved(sndr.first_name), sndr.url, returnNoneReserved(target.first_name), target.url, action_addition),
                    parse_mode = 'MarkdownV2'
                )
            if action in actions[1]:
                await msg.answer(
                '[{}]({}) *укусил\(\-а\)* [{}]({})*{}* \| 😼'.format(returnNoneReserved(sndr.first_name), sndr.url, returnNoneReserved(target.first_name), target.url, action_addition),
                    parse_mode = 'MarkdownV2'
                )
            if action in actions[2]:
                await msg.answer(
                '[{}]({}) *дал\(\-а\) шоколадку* [{}]({})*{}* \| 🍫'.format(returnNoneReserved(sndr.first_name), sndr.url, returnNoneReserved(target.first_name), target.url, action_addition),
                    parse_mode = 'MarkdownV2'
                )
            if action in actions[3]:
                await msg.answer(
                '[{}]({}) *послал\(\-а\)* [{}]({}) *спать*,*{}* \| 🛏'.format(returnNoneReserved(sndr.first_name), sndr.url, returnNoneReserved(target.first_name), target.url, action_addition),
                    parse_mode = 'MarkdownV2'
                )
            if action in actions[4]:
                await msg.answer(
                '[{}]({}) *оставил\(\-а\) засос на* [{}]({})*{}* \| 💋'.format(returnNoneReserved(sndr.first_name), sndr.url, returnNoneReserved(target.first_name), target.url, action_addition),
                    parse_mode = 'MarkdownV2'
                )
            if action in actions[5]:
                await msg.answer(
                '[{}]({}) *занялся\(\-лась\) сексом с* [{}]({})*{}* \| 👉🏻👌🏻'.format(returnNoneReserved(sndr.first_name), sndr.url, returnNoneReserved(target.first_name), target.url, action_addition),
                    parse_mode = 'MarkdownV2'
                )

        if action in actions_m or action in actions_f:
            target = msg.reply_to_message.from_user

            await msg.answer(
                '[{}]({}) *{}* [{}]({})*{}* \| 💬'.format(
                    returnNoneReserved(sndr.first_name),
                    sndr.url,
                    returnNoneReserved(action),
                    returnNoneReserved(target.first_name),
                    target.url,
                    action_addition
                ),
                parse_mode = 'MarkdownV2'
            )
    except Exception as e:
        print(e)