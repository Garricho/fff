import aiogram

from aiogram import Bot, Dispatcher

bot = Bot(token="123")
dp = Dispatcher()

async def main():
    await dp.start_polling(bot)


