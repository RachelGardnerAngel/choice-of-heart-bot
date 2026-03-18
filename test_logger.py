# test_logger.py - временный файл для проверки логирования
print("🚀 Запускаем проверку логирования...")

try:
    # Пробуем импортировать наш логгер
    from utils.logger import logger
    
    # Пишем тестовые сообщения
    logger.debug("🔍 Это DEBUG-сообщение (самое подробное)")
    logger.info("ℹ️ Это INFO-сообщение (обычная информация)")
    logger.warning("⚠️ Это WARNING-сообщение (предупреждение)")
    logger.error("❌ Это ERROR-сообщение (ошибка)")
    
    print("✅ Логирование работает!")
    print("📁 Проверь папку 'logs' и файл 'bot.log' внутри")
    
except Exception as e:
    print(f"❌ Ошибка при проверке: {e}")
    print("Проверь, что файл utils/logger.py существует и в нем нет ошибок")

input("\nНажми Enter, чтобы закрыть...")