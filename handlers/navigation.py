# handlers/navigation.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import BACK_BUTTON, BACK_MESSAGE
from keyboards.reply_kb import get_main_keyboard
from utils.logger import logger

router = Router()

@router.message(F.text == BACK_BUTTON)
async def go_back(message: Message):
    """Обработчик кнопки Назад для главного меню"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} вернулся в главное меню")
    
    await message.answer(
        text=BACK_MESSAGE,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )