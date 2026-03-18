import os
from dotenv import load_dotenv

# Загружаем переменные из .env файла
load_dotenv()

# Токен бота (обязательная переменная)
BOT_TOKEN = os.getenv("BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("Нет токена бота! Проверь файл .env")

# Настройки бота (потом можно добавить ещё)
BOT_NAME = "Choice Of Heart"
BOT_VERSION = "1.0.0"

# Настройки логирования
LOG_LEVEL = "INFO"  # Можно менять на "DEBUG" для отладки
LOG_FORMAT = "%(asctime)s - %(levelname)s - %(name)s - %(message)s"
LOG_FILE = "logs/bot.log"  # Файл для логов

# Настройки для стабильности (из-за замедления Telegram)
TELEGRAM_API_TIMEOUT = 30  # Таймаут в секундах
TELEGRAM_POLLING_TIMEOUT = 30  # Таймаут для long polling