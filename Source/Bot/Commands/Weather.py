from aiogram import types
from ..Bot import walle
from ...Utils.WeatherClient.ClientInit import mgr
from ...Utils.WeatherClient.ClientInit import Weather
from ...Utils.ReturnNoneReservesFunc import returnNoneReserved
from ..Strings.RU.Commands.Weather.WeatherInfoText import weather_info_text


async def weather_command(msg: types.Message):
    try:
        msg_place = msg.text.split()[0]

        client = Weather(msg_place)
        weather_text = client.run()

        await msg.reply(
            weather_info_text.format(
                weather_text[0],
                weather_text[1],
                returnNoneReserved(weather_text[2])
            ),
            parse_mode = 'MarkdownV2'
        )
    except Exception as e:
        pass
