# keyboards/reply_kb.py
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from utils.texts import (
    CATEGORY_YAOI, CATEGORY_YURI, CATEGORY_GET,
    BUTTON_STATS, BUTTON_DIARY, BUTTON_SUBSCRIBE
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
        width=3  # три кнопки в ряд
    )
    
    # Добавляем кнопки меню (каждая на новой строке)
    builder.row(KeyboardButton(text=BUTTON_STATS))
    builder.row(KeyboardButton(text=BUTTON_DIARY))
    builder.row(KeyboardButton(text=BUTTON_SUBSCRIBE))
    
    # Настраиваем клавиатуру
    keyboard = builder.as_markup(
        resize_keyboard=True,  # автоматический размер
        input_field_placeholder="Выбери категорию или открой меню..."
    )
    
    return keyboard