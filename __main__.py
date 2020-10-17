import logging
from aiogram import executor
from Source.Bot.Dispatcher import dp

# Configure logging
logging.basicConfig(level=logging.INFO)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
