import time
import threading
from aiogram.types import CallbackQuery
from aiogram import types
from ...Strings.RU.Commands.DuelGame.GameKeyboard import game_keyboard


class Duel():
    def __init__(self, msg: types.Message):
        self.msg = msg
        self.chat = msg.chat
        self.player1 = self.msg.from_user
        self.player2 = self.msg.reply_to_message

    async def start_game(self):
        try:
            if self.player2 is None:
                await self.msg.reply(
                    "Point someone"
                )
            else:
                await self.msg.reply(
                    "Game starting\n First player: {}\nSecond player: {}".format(self.player1, self.player2),
                    reply_markup = game_keyboard
                )
        except Exception as e:
            print(e)

    async def waiting_for_target(self):
        pass

    async def end_game(self):
        pass
