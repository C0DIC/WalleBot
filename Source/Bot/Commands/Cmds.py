from aiogram import types
from ..Bot import walle

async def cmds_command(msg: types.Message):
    try:
        walle_commands = [command for command in await walle.get_my_commands()]
        cmds_command_text = ''

        for times in range(0, len(walle_commands)):
            cmds_command_text += walle_commands[times].description + ': /' + walle_commands[times].command + '\n'

        await msg.answer(
            cmds_command_text
        )

    except Exception as e:
        print(e)