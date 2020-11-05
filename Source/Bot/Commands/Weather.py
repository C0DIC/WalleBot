from aiogram import types
from ..Bot import walle
from ...Utils.WeatherClient.ClientInit import mgr
from ...Utils.WeatherClient.ClientInit import Weather
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.RU.Commands.Weather.WeatherInfoText import weather_info_text


async def weather_command(msg: types.Message):
    try:
        msg_place = msg.text.split()[0]

        client = Weather(mgr, msg_place)

        await msg.reply(
            weather_info_text.format(
                client.temp,
                client.feels_like,
                returnNoneReserved(client.wind)
            ),
            parse_mode = 'MarkdownV2'
        )
    except Exception as e:
        pass