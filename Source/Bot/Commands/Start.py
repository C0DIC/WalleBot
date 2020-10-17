from aiogram import types
from ..Bot import walle
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.GroupLink.GroupLinkText import group_link
from ..Strings.RU.Commands.UseCommandInPrivate import use_in_private
from ..Strings.RU.Commands.StartCommandText import start_text

async def start_command(msg: types.Message):
    try:
        chat_type = msg.chat.type
        sndr = msg.from_user

        if chat_type == 'private':
            await msg.answer(
                start_text.format(
                    returnNoneReserved(sndr.first_name),
                    group_link
                ),
                parse_mode = 'MarkdownV2'
            )
            await msg.delete()
        else:
            await msg.reply(
                use_in_private.format(
                    returnNoneReserved(sndr.first_name)
                ),
                parse_mode = 'MarkdownV2'
            )
            await msg.delete()
    except Exception as e:
        print(e)
