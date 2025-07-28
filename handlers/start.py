from aiogram import Router, types, F
from keyboards import main_menu

router = Router()

@router.message(F.command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Используй кнопки меню: Кошелёк, Профиль и т.д.",
        reply_markup=main_menu()
    )
