from aiogram import Dispatcher
from .Bot import walle


# Importing bot commands
from .Commands.Start import start_command
from .Commands.Cmds import cmds_command
from .Commands.NewMembers import new_group_user
from .Commands.LeftChatMember import left_group_user
from .Commands.TotalMessages import get_total_messages
from .Commands.RemoveSystemMessages import remove_system_msg

dp = Dispatcher(walle)

dp.register_message_handler(cmds_command, commands = ['cmds'])
dp.register_message_handler(start_command, commands = ['start'])
dp.register_message_handler(get_total_messages, commands = ['stat'])
dp.register_message_handler(new_group_user, content_types = ['new_chat_members'])
dp.register_message_handler(left_group_user, content_types = ['left_chat_member'])
dp.register_message_handler(remove_system_msg, content_types = ['text'])
