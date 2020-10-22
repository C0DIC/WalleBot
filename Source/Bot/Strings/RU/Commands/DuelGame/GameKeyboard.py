from aiogram import types

yes_button = types.InlineKeyboardButton('Да!', callback_data = 'yes')
no_button = types.InlineKeyboardButton('Нет!', callback_data = 'no')

game_keyboard = types.InlineKeyboardMarkup(2, list(yes_button, no_button))