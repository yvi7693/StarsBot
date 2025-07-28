import asyncio
import logging

from aiogram import Bot, Dispatcher
from config import BOT_TOKEN

from handlers.wallet import router as wallet_router
from handlers.profile import router as profile_router
from handlers.start import router as start_router  # <-- импортируем новый роутер

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(start_router)   # <-- добавляем сюда
    dp.include_router(wallet_router)
    dp.include_router(profile_router)

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
