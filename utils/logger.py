import logging
import sys
from pathlib import Path
from config.settings import LOG_LEVEL, LOG_FORMAT, LOG_FILE

# Создаем папку для логов, если её нет
log_dir = Path("logs")
log_dir.mkdir(exist_ok=True)

# Путь к файлу с логами (исправлено! убрали лишнее)
log_path = log_dir / "bot.log"

# Настраиваем логирование
def setup_logger():
    """Настройка системы логирования"""
    
    # Создаем форматтер (как будут выглядеть записи)
    formatter = logging.Formatter(LOG_FORMAT)
    
    # Хендлер для файла (пишет в файл)
    file_handler = logging.FileHandler(
        log_path, 
        encoding='utf-8',
        mode='a'  # 'a' значит дописывать в конец файла
    )
    file_handler.setFormatter(formatter)
    file_handler.setLevel(LOG_LEVEL)
    
    # Хендлер для консоли (выводит в терминал)
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(formatter)
    console_handler.setLevel(LOG_LEVEL)
    
    # Настраиваем корневой логгер
    logger = logging.getLogger()
    logger.setLevel(LOG_LEVEL)
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    
    # Логируем запуск системы логирования (иронично, да?)
    logger.info("✅ Система логирования запущена")
    logger.info(f"📁 Логи сохраняются в: {log_path}")
    
    return logger

# Создаем логгер, который можно импортировать в другие файлы
logger = setup_logger()