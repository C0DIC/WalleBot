from aiogram import types

yes_button = types.InlineKeyboardButton('Да!', callback_data = 'yes')
no_button = types.InlineKeyboardButton('Нет!', callback_data = 'no')

buttons_list = [yes_button, no_button]

game_keyboard = types.InlineKeyboardMarkup(2, buttons_list)