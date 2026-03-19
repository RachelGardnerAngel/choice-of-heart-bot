# handlers/categories.py
import os
from aiogram import Router, F
from aiogram.types import Message, FSInputFile

from utils.texts import (
    CATEGORY_YAOI, CATEGORY_YURI, CATEGORY_GET,
    DESCRIPTION_YAOI, DESCRIPTION_YURI, DESCRIPTION_GET,
    CATEGORY_YAOI_IMAGE, CATEGORY_YURI_IMAGE, CATEGORY_GET_IMAGE,
    GENDER_FEMALE, GENDER_MALE, GENDER_CHOICE_MESSAGE,
    SUBGENRE_BUTTON_YAOI, SUBGENRE_BUTTON_YURI
)
from keyboards.reply_kb import get_category_keyboard, get_gender_keyboard, get_main_keyboard
from utils.logger import logger

router = Router()

async def send_category_with_image(message: Message, description: str, image_path: str, category_type: str):
    """Отправляет описание категории с картинкой"""
    try:
        if os.path.exists(image_path):
            photo = FSInputFile(image_path)
            await message.answer_photo(
                photo=photo,
                caption=description,
                reply_markup=get_category_keyboard(category_type),
                parse_mode="HTML"
            )
        else:
            await message.answer(
                text=description,
                reply_markup=get_category_keyboard(category_type),
                parse_mode="HTML"
            )
        logger.info(f"Категория {category_type} отправлена пользователю {message.from_user.id}")
    except Exception as e:
        logger.error(f"Ошибка при отправке категории {category_type}: {e}")
        await message.answer(
            text=description,
            reply_markup=get_category_keyboard(category_type),
            parse_mode="HTML"
        )

@router.message(F.text == CATEGORY_YAOI)
async def show_yaoi_category(message: Message):
    await send_category_with_image(
        message=message,
        description=DESCRIPTION_YAOI,
        image_path=CATEGORY_YAOI_IMAGE,
        category_type="yaoi"
    )

@router.message(F.text == CATEGORY_YURI)
async def show_yuri_category(message: Message):
    await send_category_with_image(
        message=message,
        description=DESCRIPTION_YURI,
        image_path=CATEGORY_YURI_IMAGE,
        category_type="yuri"
    )

@router.message(F.text == CATEGORY_GET)
async def show_get_category(message: Message):
    """Для Гет показываем выбор пола вместо сразу поджанров"""
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл категорию Гет")
    
    try:
        if os.path.exists(CATEGORY_GET_IMAGE):
            photo = FSInputFile(CATEGORY_GET_IMAGE)
            await message.answer_photo(
                photo=photo,
                caption=GENDER_CHOICE_MESSAGE,
                reply_markup=get_gender_keyboard(),
                parse_mode="HTML"
            )
        else:
            await message.answer(
                text=GENDER_CHOICE_MESSAGE,
                reply_markup=get_gender_keyboard(),
                parse_mode="HTML"
            )
    except Exception as e:
        logger.error(f"Ошибка при отправке выбора пола: {e}")
        await message.answer(
            text=GENDER_CHOICE_MESSAGE,
            reply_markup=get_main_keyboard(),
            parse_mode="HTML"
        )