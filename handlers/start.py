# handlers/start.py
from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command

from utils.texts import WELCOME_MESSAGE, WELCOME_IMAGE_PATH
from keyboards.reply_kb import get_main_keyboard
from utils.logger import logger

import os

router = Router()

@router.message(Command("start"))
async def cmd_start(message: Message):
    """
    Обработчик команды /start
    Отправляет приветствие с картинкой из папки images и клавиатурой
    """
    user_id = message.from_user.id
    username = message.from_user.first_name or "Читатель"
    
    logger.info(f"Пользователь {username} (ID: {user_id}) запустил бота")
    
    try:
        # Проверяем, существует ли файл с картинкой
        if os.path.exists(WELCOME_IMAGE_PATH):
            # Создаем объект FSInputFile для отправки файла
            photo = FSInputFile(WELCOME_IMAGE_PATH)
            
            # Отправляем фото с подписью
            await message.answer_photo(
                photo=photo,
                caption=WELCOME_MESSAGE,
                reply_markup=get_main_keyboard(),
                parse_mode="HTML"
            )
            logger.info(f"Приветствие с локальной картинкой отправлено пользователю {user_id}")
        else:
            # Если картинки нет, отправляем только текст
            logger.warning(f"Файл картинки {WELCOME_IMAGE_PATH} не найден")
            await message.answer(
                text=WELCOME_MESSAGE,
                reply_markup=get_main_keyboard(),
                parse_mode="HTML"
            )
        
    except Exception as e:
        logger.error(f"Ошибка при отправке приветствия пользователю {user_id}: {e}")
        await message.answer(
            "Читатель, что-то пошло не так... Попробуй ещё раз позже.",
            parse_mode="HTML"
        )