from aiogram import types
from ..Bot import walle
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.GroupLink.GroupRulesLink import rules_link
from ..Strings.RU.Commands.GreetingNewGroupUser import greetings_text


async def new_group_user(msg: types.Message):
    try:
        for times in range(0, len(msg.new_chat_members)):
            newbie = msg.new_chat_members[times]

            await msg.answer(
                greetings_text.format(
                    returnNoneReserved(newbie.first_name),
                    newbie.url,
                    rules_link
                ),
                parse_mode = 'MarkdownV2',
                disable_web_page_preview = True
            )
    except Exception as e:
        print(e)
