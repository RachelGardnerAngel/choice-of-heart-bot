# keyboards/reply_kb.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.texts import (
    CATEGORY_YAOI, CATEGORY_YURI, CATEGORY_GET,
    BUTTON_STATS, BUTTON_DIARY, BUTTON_SUBSCRIBE,
    SUBGENRE_BUTTON_YAOI, SUBGENRE_BUTTON_YURI, SUBGENRE_BUTTON_GET
)

def get_main_keyboard() -> ReplyKeyboardMarkup:
    """
    Создает главную клавиатуру с категориями и меню
    """
    builder = ReplyKeyboardBuilder()
    
    # Добавляем кнопки категорий (в один ряд)
    builder.row(
        KeyboardButton(text=CATEGORY_YAOI),
        KeyboardButton(text=CATEGORY_YURI),
        KeyboardButton(text=CATEGORY_GET),
        width=3
    )
    
    # Добавляем кнопки меню (каждая на новой строке)
    builder.row(KeyboardButton(text=BUTTON_STATS))
    builder.row(KeyboardButton(text=BUTTON_DIARY))
    builder.row(KeyboardButton(text=BUTTON_SUBSCRIBE))
    
    keyboard = builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выбери категорию или открой меню..."
    )
    
    return keyboard

def get_subgenre_keyboard(category: str) -> ReplyKeyboardMarkup:
    """
    Создает клавиатуру с кнопкой для поджанров конкретной категории
    и главным меню внизу
    """
    builder = ReplyKeyboardBuilder()
    
    # Добавляем кнопку поджанров в зависимости от категории
    if category == "yaoi":
        builder.row(KeyboardButton(text=SUBGENRE_BUTTON_YAOI))
    elif category == "yuri":
        builder.row(KeyboardButton(text=SUBGENRE_BUTTON_YURI))
    elif category == "get":
        builder.row(KeyboardButton(text=SUBGENRE_BUTTON_GET))
    
    # Добавляем кнопки главного меню
    builder.row(
        KeyboardButton(text=CATEGORY_YAOI),
        KeyboardButton(text=CATEGORY_YURI),
        KeyboardButton(text=CATEGORY_GET),
        width=3
    )
    builder.row(KeyboardButton(text=BUTTON_STATS))
    builder.row(KeyboardButton(text=BUTTON_DIARY))
    builder.row(KeyboardButton(text=BUTTON_SUBSCRIBE))
    
    keyboard = builder.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Выбери поджанр или вернись к категориям..."
    )
    
    return keyboard