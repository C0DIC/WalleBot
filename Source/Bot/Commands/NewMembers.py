import asyncio
from aiogram import types
from ..Bot import walle
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.GroupLink.GroupRulesLink import rules_link
from ..Strings.RU.Commands.MemberJoined import joined_user
from ..Strings.RU.Commands.UserAdded import added_user
from ..Strings.RU.Commands.GreetingNewGroupUser import greetings_text_assets, greetings_text


async def new_group_user(msg: types.Message):
    try:
        sndr = msg.from_user

        for times in range(0, len(msg.new_chat_members)):
            newbie = msg.new_chat_members[times]

            if msg.chat.title == 'ᴀssᴇᴛs™':
                await msg.answer(
                    greetings_text_assets.format(
                        returnNoneReserved(newbie.first_name),
                        newbie.url,
                        rules_link
                    ),
                    parse_mode = 'MarkdownV2',
                    disable_web_page_preview = True
                )
            else:
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
                        returnNoneReserved('{}-{}-{} {}:{}:{}'.format(
                                str(msg.date.day),
                                str(msg.date.month),
                                str(msg.date.year),
                                str(msg.date.hour+4),
                                str(msg.date.minute),
                                str(msg.date.second)
                        ))
                        ),
                        parse_mode = 'MarkdownV2'
                    )

        await asyncio.sleep(5)

        for times in range(0, len(msg.new_chat_members)):
            await msg.delete()

    except Exception as e:
        print(e)
