# handlers/subgenres.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import (
    SUBGENRE_BUTTON_YAOI, SUBGENRE_BUTTON_YURI, SUBGENRE_BUTTON_GET,
    SUBGENRE_PLACEHOLDER
)
from keyboards.reply_kb import get_back_only_keyboard  # новая функция для клавиатуры только с "Назад"
from utils.logger import logger

router = Router()

@router.message(F.text == SUBGENRE_BUTTON_YAOI)
async def show_yaoi_subgenres(message: Message):
    """Заглушка для поджанров Яой"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} запросил поджанры Яой")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_back_only_keyboard(),  # Только кнопка "Назад"!
        parse_mode="HTML"
    )

@router.message(F.text == SUBGENRE_BUTTON_YURI)
async def show_yuri_subgenres(message: Message):
    """Заглушка для поджанров Юри"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} запросил поджанры Юри")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_back_only_keyboard(),  # Только кнопка "Назад"!
        parse_mode="HTML"
    )

@router.message(F.text == SUBGENRE_BUTTON_GET)
async def show_get_subgenres(message: Message):
    """Заглушка для поджанров Гет"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} запросил поджанры Гет")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_back_only_keyboard(),  # Только кнопка "Назад"!
        parse_mode="HTML"
    )