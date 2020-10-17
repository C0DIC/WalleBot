from aiogram import types
from ..Bot import walle
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.GroupLink.GroupRulesLink import rules_link
from ..Strings.RU.Commands.MemberJoined import joined_user
from ..Strings.RU.Commands.UserAdded import added_user
from ..Strings.RU.Commands.GreetingNewGroupUser import greetings_text


async def new_group_user(msg: types.Message):
    try:
        sndr = msg.from_user

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

            if sndr.first_name == newbie.first_name:
                await walle.send_message(
                    -1001471262276,
                    joined_user.format(
                        returnNoneReserved(newbie.first_name),
                        newbie.url,
                    ),
                    parse_mode = 'MarkdownV2'
                )
            else:
                await walle.send_message(
                    -1001471262276,
                    added_user.format(
                        returnNoneReserved(sndr.first_name),
                        sndr.url,
                        returnNoneReserved(newbie.first_name),
                        newbie.url,
                        returnNoneReserved(sndr.first_name),
                        str(msg.date)
                    ),
                    parse_mode = 'MarkdownV2'
                )
    except Exception as e:
        print(e)
