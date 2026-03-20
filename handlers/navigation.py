# handlers/navigation.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import BACK_BUTTON, BACK_MESSAGE
from keyboards.reply_kb import get_main_keyboard, get_fantasy_keyboard
from utils.logger import logger

router = Router()

# Импортируем состояние из fantasy.py
from handlers.fantasy import user_fantasy_state
from utils.texts import (
    FANTASY_INTRO_YAOI, FANTASY_INTRO_YURI,
    FANTASY_INTRO_GET_FEMALE, FANTASY_INTRO_GET_MALE
)

@router.message(F.text == BACK_BUTTON)
async def go_back(message: Message):
    """Обработчик кнопки Назад — с учётом состояния Фэнтези"""
    user_id = message.from_user.id
    
    # Проверяем, не в Фэнтези ли пользователь
    fantasy_state = user_fantasy_state.get(user_id)
    
    if fantasy_state:
        # Пользователь в Фэнтези! Обрабатываем здесь
        category = fantasy_state.get("category")
        level = fantasy_state.get("level")
        
        logger.info(f"Пользователь {user_id} нажал Назад в Фэнтези. Уровень: {level}, категория: {category}")
        
        if level == "settings_list":
            # Возвращаемся в поджанры
            from handlers.fantasy import back_to_subgenres
            await back_to_subgenres(message, category)
            return
            
        elif level == "setting_description":
            # Возвращаемся к списку сеттингов
            if category == "yaoi":
                text = FANTASY_INTRO_YAOI
                keyboard = get_fantasy_keyboard("yaoi")
            elif category == "yuri":
                text = FANTASY_INTRO_YURI
                keyboard = get_fantasy_keyboard("yuri")
            elif category == "get_female":
                text = FANTASY_INTRO_GET_FEMALE
                keyboard = get_fantasy_keyboard("get_female")
            elif category == "get_male":
                text = FANTASY_INTRO_GET_MALE
                keyboard = get_fantasy_keyboard("get_male")
            else:
                await message.answer(
                    text=BACK_MESSAGE,
                    reply_markup=get_main_keyboard(),
                    parse_mode="HTML"
                )
                return
            
            # Обновляем состояние
            user_fantasy_state[user_id]["level"] = "settings_list"
            
            await message.answer(
                text=text,
                reply_markup=keyboard,
                parse_mode="HTML"
            )
            return
    
    # Если не в Фэнтези — обычное возвращение в главное меню
    logger.info(f"Пользователь {user_id} вернулся в главное меню")
    await message.answer(
        text=BACK_MESSAGE,
        reply_markup=get_main_keyboard(),
        parse_mode="HTML"
    )