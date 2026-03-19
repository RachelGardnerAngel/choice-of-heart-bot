# handlers/subgenres.py
from aiogram import Router, F
from aiogram.types import Message

from utils.texts import (
    SUBGENRE_BUTTON_YAOI, SUBGENRE_BUTTON_YURI,
    SUBGENRE_INTRO_YAOI, SUBGENRE_INTRO_YURI,
    SUBGENRE_INTRO_GET_FEMALE, SUBGENRE_INTRO_GET_MALE,
    GENDER_FEMALE, GENDER_MALE,
    GENDER_CHOICE_BACK_MESSAGE,
    SUBGENRES_YAOI, SUBGENRES_YURI,
    SUBGENRES_GET_FEMALE, SUBGENRES_GET_MALE,
    BACK_BUTTON, SUBGENRE_PLACEHOLDER
)
from keyboards.reply_kb import (
    get_subgenre_keyboard, get_gender_keyboard,
    get_back_only_keyboard, get_main_keyboard
)
from utils.logger import logger

router = Router()

# Хранилище для выбранного пола (временное, потом заменим на БД)
user_gender = {}

# ===== ЯОЙ =====
@router.message(F.text == SUBGENRE_BUTTON_YAOI)
async def show_yaoi_subgenres(message: Message):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл поджанры Яой")
    
    await message.answer(
        text=SUBGENRE_INTRO_YAOI,
        reply_markup=get_subgenre_keyboard("yaoi"),
        parse_mode="HTML"
    )

# ===== ЮРИ =====
@router.message(F.text == SUBGENRE_BUTTON_YURI)
async def show_yuri_subgenres(message: Message):
    user_id = message.from_user.id
    logger.info(f"Пользователь {user_id} открыл поджанры Юри")
    
    await message.answer(
        text=SUBGENRE_INTRO_YURI,
        reply_markup=get_subgenre_keyboard("yuri"),
        parse_mode="HTML"
    )

# ===== ГЕТ: выбор пола =====
@router.message(F.text == GENDER_FEMALE)
async def choose_female(message: Message):
    user_id = message.from_user.id
    user_gender[user_id] = "female"
    logger.info(f"Пользователь {user_id} выбрал ГГ девушку")
    
    await message.answer(
        text=SUBGENRE_INTRO_GET_FEMALE,
        reply_markup=get_subgenre_keyboard("get", "female"),
        parse_mode="HTML"
    )

@router.message(F.text == GENDER_MALE)
async def choose_male(message: Message):
    user_id = message.from_user.id
    user_gender[user_id] = "male"
    logger.info(f"Пользователь {user_id} выбрал ГГ парня")
    
    await message.answer(
        text=SUBGENRE_INTRO_GET_MALE,
        reply_markup=get_subgenre_keyboard("get", "male"),
        parse_mode="HTML"
    )

# ===== ОБРАБОТКА ПОДЖАНРОВ =====
# Яой
@router.message(F.text.in_(SUBGENRES_YAOI))
async def handle_yaoi_subgenre(message: Message):
    user_id = message.from_user.id
    subgenre = message.text
    logger.info(f"Пользователь {user_id} выбрал поджанр в Яой: {subgenre[:30]}...")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_subgenre_keyboard("yaoi"),  # возврат к списку поджанров
        parse_mode="HTML"
    )

# Юри
@router.message(F.text.in_(SUBGENRES_YURI))
async def handle_yuri_subgenre(message: Message):
    user_id = message.from_user.id
    subgenre = message.text
    logger.info(f"Пользователь {user_id} выбрал поджанр в Юри: {subgenre[:30]}...")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_subgenre_keyboard("yuri"),
        parse_mode="HTML"
    )

# Гет (девушка)
@router.message(F.text.in_(SUBGENRES_GET_FEMALE))
async def handle_get_female_subgenre(message: Message):
    user_id = message.from_user.id
    subgenre = message.text
    logger.info(f"Пользователь {user_id} выбрал поджанр в Гет (дев): {subgenre[:30]}...")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_subgenre_keyboard("get", "female"),
        parse_mode="HTML"
    )

# Гет (парень)
@router.message(F.text.in_(SUBGENRES_GET_MALE))
async def handle_get_male_subgenre(message: Message):
    user_id = message.from_user.id
    subgenre = message.text
    logger.info(f"Пользователь {user_id} выбрал поджанр в Гет (пар): {subgenre[:30]}...")
    
    await message.answer(
        text=SUBGENRE_PLACEHOLDER,
        reply_markup=get_subgenre_keyboard("get", "male"),
        parse_mode="HTML"
    )

# ===== ОБРАБОТКА НАЗАД В ГЕТ =====
@router.message(F.text == BACK_BUTTON)
async def handle_back_in_get(message: Message):
    user_id = message.from_user.id
    
    # Если пользователь был в поджанрах Гет, возвращаем к выбору пола
    if user_id in user_gender:
        gender = user_gender[user_id]
        logger.info(f"Пользователь {user_id} вернулся к выбору пола из поджанров Гет ({gender})")
        
        await message.answer(
            text=GENDER_CHOICE_BACK_MESSAGE,
            reply_markup=get_gender_keyboard(),
            parse_mode="HTML"
        )
        # Не удаляем gender, чтобы запомнить, откуда пришёл
    else:
        # Если не в Гет, передаём в navigation.py
        from handlers.navigation import go_back
        await go_back(message)