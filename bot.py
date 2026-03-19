#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Choice Of Heart - основной файл запуска бота
"""

import asyncio
import time
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from config.settings import BOT_TOKEN, TELEGRAM_API_TIMEOUT, TELEGRAM_POLLING_TIMEOUT
from utils.logger import logger

# Даём время старому экземпляру завершиться
time.sleep(7)

# Подключаем все обработчики
from handlers import start, menu, categories, subgenres, navigation

# Создаем объекты бота и диспетчера
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    timeout=TELEGRAM_API_TIMEOUT
)
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(start.router)
dp.include_router(menu.router)
dp.include_router(categories.router)
dp.include_router(subgenres.router)
dp.include_router(navigation.router)

async def main():
    """Главная функция запуска бота"""
    logger.info("🚀 Запуск бота Choice Of Heart...")
    logger.info(f"🤖 Токен: {BOT_TOKEN[:10]}... (скрыто)")
    logger.info(f"⏱️ Таймаут API: {TELEGRAM_API_TIMEOUT} сек")
    logger.info(f"⏱️ Polling таймаут: {TELEGRAM_POLLING_TIMEOUT} сек")
    
    try:
        await dp.start_polling(
            bot,
            allowed_updates=dp.resolve_used_update_types(),
            timeout=TELEGRAM_API_TIMEOUT,
            polling_timeout=TELEGRAM_POLLING_TIMEOUT
        )
    except Exception as e:
        logger.error(f"❌ Критическая ошибка: {e}")
    finally:
        logger.info("🛑 Бот остановлен")

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        logger.info("👋 Бот остановлен пользователем")
    except Exception as e:
        logger.error(f"💥 Непредвиденная ошибка: {e}")