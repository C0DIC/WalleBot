from aiogram import Dispatcher
from .Bot import walle


# Importing bot commands
from .Commands.Start import start_command
from .Commands.Cmds import cmds_command
from .Commands.NewMembers import new_group_user
from .Commands.LeftChatMember import left_group_user
from .Commands.TotalMessages import get_total_messages
from .Commands.RemoveSystemMessages import remove_system_msg
from .Commands.Mute import mute_command
from .Commands.Unmute import unmute_command
from .Commands.Ban import ban_command
from .Commands.Unban import unban_command
from .Commands.Pin import pin_command
from .Commands.StatForDay import day_stat_command


dp = Dispatcher(walle)

# Default
dp.register_message_handler(cmds_command, commands = ['cmds'])
dp.register_message_handler(start_command, commands = ['start'])
dp.register_message_handler(get_total_messages, commands = ['stat'])
dp.register_message_handler(day_stat_command, commands = ['day_stat'])

# Events
dp.register_message_handler(new_group_user, content_types = ['new_chat_members'])
dp.register_message_handler(left_group_user, content_types = ['left_chat_member'])
dp.register_message_handler(dp.async_task(remove_system_msg), content_types = ['pinned_message'])

# Moderation
dp.register_message_handler(mute_command, commands = ['mute'], commands_prefix = '*')
dp.register_message_handler(unmute_command, commands = ['unmute'], commands_prefix = '*')
dp.register_message_handler(ban_command, commands = ['ban'], commands_prefix = '*')
dp.register_message_handler(unban_command, commands = ['unban'], commands_prefix = '*')
dp.register_message_handler(pin_command, commands = ['pin'], commands_prefix = '*')
