from aiogram import Dispatcher
from .Bot import walle


# Importing bot commands
from .Commands.Start import start_command


dp = Dispatcher(walle)

dp.register_message_handler(start_command, commands = ['start'])