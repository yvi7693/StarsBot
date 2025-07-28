import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from config import BOT_TOKEN

from handlers.wallet import router as wallet_router
from handlers.profile import router as profile_router

logging.basicConfig(level=logging.INFO)

async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()
    dp.include_router(wallet_router)
    dp.include_router(profile_router)

    @dp.message(F.command("start"))
    async def cmd_start(message: types.Message):
        await message.answer("Привет! Используй кнопки меню: Кошелёк, Профиль и т.д.")

    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())