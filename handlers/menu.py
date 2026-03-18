# handlers/menu.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import (
    BUTTON_STATS, BUTTON_DIARY, BUTTON_SUBSCRIBE,
    STATS_PLACEHOLDER, DIARY_PLACEHOLDER, SUBSCRIBE_PLACEHOLDER
)
from keyboards.reply_kb import get_main_keyboard
from utils.logger import logger

router = Router()

@router.message(F.text == BUTTON_STATS)
async def show_stats(message: Message):
    """Показывает статистику пользователя (заглушка)"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} запросил статистику")
    
    await message.answer(
        text=STATS_PLACEHOLDER,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )

@router.message(F.text == BUTTON_DIARY)
async def show_diary(message: Message):
    """Показывает дневник автора (заглушка)"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл дневник автора")
    
    await message.answer(
        text=DIARY_PLACEHOLDER,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )

@router.message(F.text == BUTTON_SUBSCRIBE)
async def show_subscribe(message: Message):
    """Показывает информацию о подписке (заглушка)"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} запросил информацию о подписке")
    
    await message.answer(
        text=SUBSCRIBE_PLACEHOLDER,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )