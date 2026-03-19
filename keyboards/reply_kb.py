# keyboards/reply_kb.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.texts import (
    CATEGORY_YAOI, CATEGORY_YURI, CATEGORY_GET,
    BUTTON_STATS, BUTTON_DIARY, BUTTON_SUBSCRIBE,
    BACK_BUTTON, GENDER_FEMALE, GENDER_MALE,
    SUBGENRES_YAOI, SUBGENRES_YURI, SUBGENRES_GET_FEMALE, SUBGENRES_GET_MALE
)

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """Главная клавиатура с категориями и меню"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text=CATEGORY_YAOI),
        KeyboardButton(text=CATEGORY_YURI),
        KeyboardButton(text=CATEGORY_GET),
        width=3
    )
    
    builder.row(KeyboardButton(text=BUTTON_STATS))
    builder.row(KeyboardButton(text=BUTTON_DIARY))
    builder.row(KeyboardButton(text=BUTTON_SUBSCRIBE))
    
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выбери категорию или открой меню..."
    )

def get_category_keyboard(category: str) -> ReplyKeyboardMarkup:
    """Клавиатура для категории (кнопка поджанров + назад)"""
    builder = ReplyKeyboardBuilder()
    
    if category == "yaoi":
        from utils.texts import SUBGENRE_BUTTON_YAOI
        builder.row(KeyboardButton(text=SUBGENRE_BUTTON_YAOI))
    elif category == "yuri":
        from utils.texts import SUBGENRE_BUTTON_YURI
        builder.row(KeyboardButton(text=SUBGENRE_BUTTON_YURI))
    elif category == "get":
        # Для Гет показываем кнопки выбора пола
        builder.row(
            KeyboardButton(text=GENDER_FEMALE),
            KeyboardButton(text=GENDER_MALE),
            width=2
        )
    
    builder.row(KeyboardButton(text=BACK_BUTTON))
    
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Сделай выбор..."
    )

def get_gender_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура только для выбора пола (после возврата)"""
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text=GENDER_FEMALE),
        KeyboardButton(text=GENDER_MALE),
        width=2
    )
    builder.row(KeyboardButton(text=BACK_BUTTON))
    
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выбери пол ГГ..."
    )

def get_subgenre_keyboard(category: str, gender: str = None) -> ReplyKeyboardMarkup:
    """Клавиатура с поджанрами для конкретной категории и пола"""
    builder = ReplyKeyboardBuilder()
    
    if category == "yaoi":
        for subgenre in SUBGENRES_YAOI:
            builder.row(KeyboardButton(text=subgenre))
    elif category == "yuri":
        for subgenre in SUBGENRES_YURI:
            builder.row(KeyboardButton(text=subgenre))
    elif category == "get" and gender == "female":
        for subgenre in SUBGENRES_GET_FEMALE:
            builder.row(KeyboardButton(text=subgenre))
    elif category == "get" and gender == "male":
        for subgenre in SUBGENRES_GET_MALE:
            builder.row(KeyboardButton(text=subgenre))
    
    builder.row(KeyboardButton(text=BACK_BUTTON))
    
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выбери жанр..."
    )

def get_back_only_keyboard() -> ReplyKeyboardMarkup:
    """Клавиатура только с кнопкой назад"""
    builder = ReplyKeyboardBuilder()
    builder.row(KeyboardButton(text=BACK_BUTTON))
    
    return builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Вернуться назад..."
    )