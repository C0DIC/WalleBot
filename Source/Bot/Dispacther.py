from aiogram import Dispatcher
from .Bot import walle


# Importing bot commands
from .Commands.Start import start_command
from .Commands.Cmds import cmds_command
from .Commands.NewMembers import new_group_user
from .Commands.LeftChatMember import left_group_user
from .Commands.Stat import stat_command
from .Commands.RemoveSystemMessages import remove_system_msg
from .Commands.Unmute import unmute_command
from .Commands.Ban import ban_command
from .Commands.Unban import unban_command
from .Commands.Pin import pin_command
from .Commands.ActionsFilter import actions_filter
from .Commands.Antiflood import antiflood
from .Commands.NewMute import mute_command


dp = Dispatcher(walle)


# Default
dp.register_message_handler(cmds_command, commands = ['cmds'])
dp.register_message_handler(start_command, commands = ['start'])
dp.register_message_handler(stat_command, commands = ['stat'])

# Moderation
dp.register_message_handler(mute_command, commands = ['mute'])
dp.register_message_handler(unmute_command, commands = ['unmute'])
dp.register_message_handler(ban_command, commands = ['ban'])
dp.register_message_handler(unban_command, commands = ['unban'])
dp.register_message_handler(pin_command, commands = ['pin'])

# Events
dp.register_message_handler(new_group_user, content_types = ['new_chat_members'])
dp.register_message_handler(left_group_user, content_types = ['left_chat_member'])
dp.register_message_handler(dp.async_task(remove_system_msg), content_types = ['pinned_message'])
dp.register_message_handler(dp.async_task(actions_filter), content_types = ['text'])