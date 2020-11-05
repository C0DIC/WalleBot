import time
import threading
from aiogram import Dispatcher
from aiogram.types import CallbackQuery
from aiogram import types
from ...Strings.RU.Commands.DuelGame.GameKeyboard import game_keyboard


class Duel(Dispatcher, CallbackQuery):
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
                    "Game starting\nFirst player: {}\nSecond player: {}".format(self.player1.first_name, self.player2.from_user.first_name),
                    reply_markup = game_keyboard
                )
        except Exception as e:
            print(e)


    #def callbak

            
    async def waiting_for_target(self):
        try:
            if self.data == 'yes':
                if self.from_user == self.player1 or self.from_user != self.player2:
                    await self.msg.answer("Error")
                else:
                    await self.msg.answer("Round started")
            elif self.data == 'no':
                if self.from_user == self.player1 or self.from_user != self.player2:
                    await self.msg.answer("Error")
                else:
                    await self.msg.answer("Round canceld")
        except Exception as e:
            print(e)

    async def end_game(self):
        pass
