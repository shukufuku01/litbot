import asyncio
import logging

from aiogram import Bot, Dispatcher

from app.handlers import router
from config import TOKEN

# Инициализация
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Основная функция
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)

# Запуск
if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")
