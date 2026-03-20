# handlers/fantasy.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import (
    SUBGENRE_YAOI_FANTASY, SUBGENRE_YURI_FANTASY,
    SUBGENRE_GET_FEMALE_FANTASY, SUBGENRE_GET_MALE_FANTASY,
    FANTASY_INTRO_YAOI, FANTASY_INTRO_YURI,
    FANTASY_INTRO_GET_FEMALE, FANTASY_INTRO_GET_MALE,
    SETTING_YAOI_1, SETTING_YAOI_2, SETTING_YAOI_3,
    SETTING_YAOI_4, SETTING_YAOI_5, SETTING_YAOI_6,
    SETTING_YURI_1, SETTING_YURI_2, SETTING_YURI_3,
    SETTING_YURI_4, SETTING_YURI_5, SETTING_YURI_6,
    SETTING_GET_FEMALE_1, SETTING_GET_FEMALE_2, SETTING_GET_FEMALE_3,
    SETTING_GET_FEMALE_4, SETTING_GET_FEMALE_5, SETTING_GET_FEMALE_6,
    SETTING_GET_MALE_1, SETTING_GET_MALE_2, SETTING_GET_MALE_3,
    SETTING_GET_MALE_4, SETTING_GET_MALE_5, SETTING_GET_MALE_6,
    DESC_YAOI_1, DESC_YAOI_2, DESC_YAOI_3, DESC_YAOI_4, DESC_YAOI_5, DESC_YAOI_6,
    DESC_YURI_1, DESC_YURI_2, DESC_YURI_3, DESC_YURI_4, DESC_YURI_5, DESC_YURI_6,
    DESC_GET_FEMALE_1, DESC_GET_FEMALE_2, DESC_GET_FEMALE_3,
    DESC_GET_FEMALE_4, DESC_GET_FEMALE_5, DESC_GET_FEMALE_6,
    DESC_GET_MALE_1, DESC_GET_MALE_2, DESC_GET_MALE_3,
    DESC_GET_MALE_4, DESC_GET_MALE_5, DESC_GET_MALE_6,
    NOVELLA_PLACEHOLDER, BACK_BUTTON
)
from keyboards.reply_kb import get_fantasy_keyboard, get_back_only_keyboard, get_subgenre_keyboard
from utils.logger import logger

router = Router()

# Хранилище для состояния пользователя в Фэнтези
# Ключ: user_id
# Значение: словарь с информацией, откуда пришёл
user_fantasy_state = {}

# ========== ФУНКЦИЯ ДЛЯ ВОЗВРАТА В ПОДЖАНРЫ ==========
async def back_to_subgenres(message: Message, category: str, gender: str = None):
    """Возвращает пользователя обратно в меню поджанров"""
    user_id = message.from_user.id
    
    if category == "yaoi":
        from handlers.subgenres import show_yaoi_subgenres
        await show_yaoi_subgenres(message)
    elif category == "yuri":
        from handlers.subgenres import show_yuri_subgenres
        await show_yuri_subgenres(message)
    elif category == "get_female":
        # Для Гет девушка — возвращаем в поджанры (уже с выбранным полом)
        from utils.texts import SUBGENRE_INTRO_GET_FEMALE
        await message.answer(
            text=SUBGENRE_INTRO_GET_FEMALE,
            reply_markup=get_subgenre_keyboard("get", "female"),
            parse_mode="HTML"
        )
    elif category == "get_male":
        from utils.texts import SUBGENRE_INTRO_GET_MALE
        await message.answer(
            text=SUBGENRE_INTRO_GET_MALE,
            reply_markup=get_subgenre_keyboard("get", "male"),
            parse_mode="HTML"
        )
    
    # Удаляем состояние, так как вернулись
    if user_id in user_fantasy_state:
        del user_fantasy_state[user_id]

# ========== ЯОЙ ==========
@router.message(F.text == SUBGENRE_YAOI_FANTASY)
async def show_fantasy_yaoi(message: Message):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл Фэнтези в Яое")
    
    # Запоминаем, откуда пришли
    user_fantasy_state[user_id] = {
        "category": "yaoi",
        "level": "settings_list"  # сейчас на экране списка сеттингов
    }
    
    await message.answer(
        text=FANTASY_INTRO_YAOI,
        reply_markup=get_fantasy_keyboard("yaoi"),
        parse_mode="HTML"
    )

# Обработчики сеттингов Яой
@router.message(F.text == SETTING_YAOI_1)
async def setting_yaoi_1(message: Message):
    await send_setting(message, DESC_YAOI_1, "yaoi", 1)

@router.message(F.text == SETTING_YAOI_2)
async def setting_yaoi_2(message: Message):
    await send_setting(message, DESC_YAOI_2, "yaoi", 2)

@router.message(F.text == SETTING_YAOI_3)
async def setting_yaoi_3(message: Message):
    await send_setting(message, DESC_YAOI_3, "yaoi", 3)

@router.message(F.text == SETTING_YAOI_4)
async def setting_yaoi_4(message: Message):
    await send_setting(message, DESC_YAOI_4, "yaoi", 4)

@router.message(F.text == SETTING_YAOI_5)
async def setting_yaoi_5(message: Message):
    await send_setting(message, DESC_YAOI_5, "yaoi", 5)

@router.message(F.text == SETTING_YAOI_6)
async def setting_yaoi_6(message: Message):
    await send_setting(message, DESC_YAOI_6, "yaoi", 6)

# ========== ЮРИ ==========
@router.message(F.text == SUBGENRE_YURI_FANTASY)
async def show_fantasy_yuri(message: Message):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл Фэнтези в Юри")
    
    user_fantasy_state[user_id] = {
        "category": "yuri",
        "level": "settings_list"
    }
    
    await message.answer(
        text=FANTASY_INTRO_YURI,
        reply_markup=get_fantasy_keyboard("yuri"),
        parse_mode="HTML"
    )

# Обработчики сеттингов Юри
@router.message(F.text == SETTING_YURI_1)
async def setting_yuri_1(message: Message):
    await send_setting(message, DESC_YURI_1, "yuri", 1)

@router.message(F.text == SETTING_YURI_2)
async def setting_yuri_2(message: Message):
    await send_setting(message, DESC_YURI_2, "yuri", 2)

@router.message(F.text == SETTING_YURI_3)
async def setting_yuri_3(message: Message):
    await send_setting(message, DESC_YURI_3, "yuri", 3)

@router.message(F.text == SETTING_YURI_4)
async def setting_yuri_4(message: Message):
    await send_setting(message, DESC_YURI_4, "yuri", 4)

@router.message(F.text == SETTING_YURI_5)
async def setting_yuri_5(message: Message):
    await send_setting(message, DESC_YURI_5, "yuri", 5)

@router.message(F.text == SETTING_YURI_6)
async def setting_yuri_6(message: Message):
    await send_setting(message, DESC_YURI_6, "yuri", 6)

# ========== ГЕТ (девушка ГГ) ==========
@router.message(F.text == SUBGENRE_GET_FEMALE_FANTASY)
async def show_fantasy_get_female(message: Message):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл Фэнтези в Гет (девушка)")
    
    user_fantasy_state[user_id] = {
        "category": "get_female",
        "level": "settings_list"
    }
    
    await message.answer(
        text=FANTASY_INTRO_GET_FEMALE,
        reply_markup=get_fantasy_keyboard("get_female"),
        parse_mode="HTML"
    )

# Обработчики сеттингов Гет (девушка)
@router.message(F.text == SETTING_GET_FEMALE_1)
async def setting_get_female_1(message: Message):
    await send_setting(message, DESC_GET_FEMALE_1, "get_female", 1)

@router.message(F.text == SETTING_GET_FEMALE_2)
async def setting_get_female_2(message: Message):
    await send_setting(message, DESC_GET_FEMALE_2, "get_female", 2)

@router.message(F.text == SETTING_GET_FEMALE_3)
async def setting_get_female_3(message: Message):
    await send_setting(message, DESC_GET_FEMALE_3, "get_female", 3)

@router.message(F.text == SETTING_GET_FEMALE_4)
async def setting_get_female_4(message: Message):
    await send_setting(message, DESC_GET_FEMALE_4, "get_female", 4)

@router.message(F.text == SETTING_GET_FEMALE_5)
async def setting_get_female_5(message: Message):
    await send_setting(message, DESC_GET_FEMALE_5, "get_female", 5)

@router.message(F.text == SETTING_GET_FEMALE_6)
async def setting_get_female_6(message: Message):
    await send_setting(message, DESC_GET_FEMALE_6, "get_female", 6)

# ========== ГЕТ (парень ГГ) ==========
@router.message(F.text == SUBGENRE_GET_MALE_FANTASY)
async def show_fantasy_get_male(message: Message):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл Фэнтези в Гет (парень)")
    
    user_fantasy_state[user_id] = {
        "category": "get_male",
        "level": "settings_list"
    }
    
    await message.answer(
        text=FANTASY_INTRO_GET_MALE,
        reply_markup=get_fantasy_keyboard("get_male"),
        parse_mode="HTML"
    )

# Обработчики сеттингов Гет (парень)
@router.message(F.text == SETTING_GET_MALE_1)
async def setting_get_male_1(message: Message):
    await send_setting(message, DESC_GET_MALE_1, "get_male", 1)

@router.message(F.text == SETTING_GET_MALE_2)
async def setting_get_male_2(message: Message):
    await send_setting(message, DESC_GET_MALE_2, "get_male", 2)

@router.message(F.text == SETTING_GET_MALE_3)
async def setting_get_male_3(message: Message):
    await send_setting(message, DESC_GET_MALE_3, "get_male", 3)

@router.message(F.text == SETTING_GET_MALE_4)
async def setting_get_male_4(message: Message):
    await send_setting(message, DESC_GET_MALE_4, "get_male", 4)

@router.message(F.text == SETTING_GET_MALE_5)
async def setting_get_male_5(message: Message):
    await send_setting(message, DESC_GET_MALE_5, "get_male", 5)

@router.message(F.text == SETTING_GET_MALE_6)
async def setting_get_male_6(message: Message):
    await send_setting(message, DESC_GET_MALE_6, "get_male", 6)

# ========== ОБЩАЯ ФУНКЦИЯ ДЛЯ СЕТТИНГОВ ==========
async def send_setting(message: Message, description: str, category: str, setting_num: int):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл сеттинг {setting_num} в {category}")
    
    # Обновляем состояние — теперь на уровне описания сеттинга
    if user_id in user_fantasy_state:
        user_fantasy_state[user_id]["level"] = "setting_description"
        user_fantasy_state[user_id]["setting_num"] = setting_num
    
    await message.answer(
        text=description,
        reply_markup=get_back_only_keyboard(),
        parse_mode="HTML"
    )

# ========== ОБРАБОТКА КНОПКИ НАЗАД ==========
@router.message(F.text == BACK_BUTTON)
async def handle_back_in_fantasy(message: Message):
    user_id = message.from_user.id
    state = user_fantasy_state.get(user_id)
    
    if not state:
        # Если не в Фэнтези, передаём дальше
        return
    
    category = state.get("category")
    level = state.get("level")
    
    logger.info(f"Пользователь {user_id} нажал Назад в Фэнтези. Уровень: {level}, категория: {category}")
    
    if level == "settings_list":
        # На экране списка сеттингов — возвращаемся в поджанры
        await back_to_subgenres(message, category)
        
    elif level == "setting_description":
        # На экране описания сеттинга — возвращаемся к списку сеттингов
        # Восстанавливаем клавиатуру с сеттингами
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
            return
        
        # Обновляем состояние
        user_fantasy_state[user_id]["level"] = "settings_list"
        
        await message.answer(
            text=text,
            reply_markup=keyboard,
            parse_mode="HTML"
        )