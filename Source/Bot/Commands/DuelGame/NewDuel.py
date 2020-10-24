import time
import random
from aiogram import types
from ...Strings.RU.Commands.DuelGame.GameKeyboard import game_keyboard
from ...Strings.RU.Commands.DuelGame.MainText import main_duel_text
from ...Strings.RU.Errors.PointTargetError import point_target
from ....Utils.ReturnNoneReservesFunc import returnNoneReserved
from .DuelCallback import Duel


async def duel_command(msg: types.Message):
    try:
        duel = Duel(msg)

        await duel.start_game()

        await duel.waiting_for_target()
    except Exception as e:
        print(e)