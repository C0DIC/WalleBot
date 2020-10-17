from aiogram import Dispatcher
from .Bot import walle


# Importing bot commands
from .Commands.Start import start_command
from .Commands.Cmds import cmds_command
from .Commands.NewMembers import new_group_user

dp = Dispatcher(walle)

dp.register_message_handler(start_command, commands = ['start'])
dp.register_message_handler(cmds_command, commands = ['cmds'])
dp.register_message_handler(new_group_user, content_types = ['new_chat_members'])