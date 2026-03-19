# handlers/categories.py
import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from utils.texts import (
    CATEGORY_YAOI, CATEGORY_YURI, CATEGORY_GET,
    DESCRIPTION_YAOI, DESCRIPTION_YURI, DESCRIPTION_GET,
    CATEGORY_YAOI_IMAGE, CATEGORY_YURI_IMAGE, CATEGORY_GET_IMAGE,
    BACK_BUTTON
)
from keyboards.reply_kb import get_category_keyboard, get_main_keyboard
from utils.logger import logger

router = Router()

async def send_category_with_image(message: Message, description: str, image_path: str, category_type: str):
    """
    Отправляет описание категории с картинкой (если есть)
    и клавиатурой только для этой категории
    """
    try:
        if os.path.exists(image_path):
            photo = FSInputFile(image_path)
            await message.answer_photo(
                photo=photo,
                caption=description,
                reply_markup=get_category_keyboard(category_type),  # теперь только две кнопки!
                parse_mode="HTML"
            )
            logger.info(f"Категория {category_type} с картинкой отправлена пользователю {message.from_user.id}")
        else:
            logger.warning(f"Файл картинки {image_path} не найден")
            await message.answer(
                text=description,
                reply_markup=get_category_keyboard(category_type),
                parse_mode="HTML"
            )
    except Exception as e:
        logger.error(f"Ошибка при отправке категории {category_type}: {e}")
        await message.answer(
            text=description,
            reply_markup=get_category_keyboard(category_type),
            parse_mode="HTML"
        )

@router.message(F.text == CATEGORY_YAOI)
async def show_yaoi_category(message: Message):
    """Показывает описание категории Яой и убирает главное меню"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Яой")
    
    await send_category_with_image(
        message=message,
        description=DESCRIPTION_YAOI,
        image_path=CATEGORY_YAOI_IMAGE,
        category_type="yaoi"
    )

@router.message(F.text == CATEGORY_YURI)
async def show_yuri_category(message: Message):
    """Показывает описание категории Юри и убирает главное меню"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Юри")
    
    await send_category_with_image(
        message=message,
        description=DESCRIPTION_YURI,
        image_path=CATEGORY_YURI_IMAGE,
        category_type="yuri"
    )

@router.message(F.text == CATEGORY_GET)
async def show_get_category(message: Message):
    """Показывает описание категории Гет и убирает главное меню"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Гет")
    
    await send_category_with_image(
        message=message,
        description=DESCRIPTION_GET,
        image_path=CATEGORY_GET_IMAGE,
        category_type="get"
    )