from aiogram import types
from ...Bot import walle
from .ActivityTablet import activity_tablet, public_tablet, makeOffline, makeOnline


async def afk_command(msg: types.Message):
    try:
        sndr = msg.from_user

        if sndr in activity_tablet:
            for i in range(0, len(public_tablet)):
                if sndr.first_name in public_tablet[i]:
                    makeOffline(public_tablet[i])
        else:
            pass
    except Exception as e:
        print(e)