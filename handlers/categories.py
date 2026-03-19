# handlers/categories.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import (
    CATEGORY_YAOI, CATEGORY_YURI, CATEGORY_GET,
    DESCRIPTION_YAOI, DESCRIPTION_YURI, DESCRIPTION_GET,
    SUBGENRE_BUTTON_YAOI, SUBGENRE_BUTTON_YURI, SUBGENRE_BUTTON_GET
)
from keyboards.reply_kb import get_main_keyboard, get_subgenre_keyboard
from utils.logger import logger

router = Router()

@router.message(F.text == CATEGORY_YAOI)
async def show_yaoi_category(message: Message):
    """Показывает описание категории Яой и кнопку к поджанрам"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Яой")
    
    await message.answer(
        text=DESCRIPTION_YAOI,
        reply_markup=get_subgenre_keyboard("yaoi"),  # клавиатура с кнопкой для Яой
        parse_mode="HTML"
    )

@router.message(F.text == CATEGORY_YURI)
async def show_yuri_category(message: Message):
    """Показывает описание категории Юри и кнопку к поджанрам"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Юри")
    
    await message.answer(
        text=DESCRIPTION_YURI,
        reply_markup=get_subgenre_keyboard("yuri"),
        parse_mode="HTML"
    )

@router.message(F.text == CATEGORY_GET)
async def show_get_category(message: Message):
    """Показывает описание категории Гет и кнопку к поджанрам"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Гет")
    
    await message.answer(
        text=DESCRIPTION_GET,
        reply_markup=get_subgenre_keyboard("get"),
        parse_mode="HTML"
    )