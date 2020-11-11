import pyowm
from pyowm.owm import OWM
from pyowm.commons.exceptions import NotFoundError
from pyowm.utils.config import get_default_config

config_dict = get_default_config()
config_dict['language'] = 'ru' # your language here

mgr = owm.weather_manager()


class Weather:
    def __init__(self, place):
        self.place = place
        self.link = OWM('e26a3a63794a69d1983e3d006a3daee5', config_dict)
        self.keep_running = True


    def run(self):
        self.mngr = self.link.weather_manager()
        self.obs = self.mngr.weather_at_place(self.place)
        self.w = self.obs.weather

        self.temp = str(self.w.temperature('celsius')['temp']).replace('.', ',')
        self.feels_like = str(self.w.temperature('celsius')['feels_like']).replace('.', ',')
        self.wind = str(self.w.wind(unit = 'meters_sec')['speed']).replace('.', ',')
        self.one_word = self.w.detailed_status.capitalize()

        self.info = [self.temp, self.feels_like, self.wind, self.one_word]

        return self.info
