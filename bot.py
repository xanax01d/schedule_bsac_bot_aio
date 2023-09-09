import asyncio
import logging
from aiogram import Bot, Dispatcher
from configs.cfg import tbt
from handlers import questions,admin

logging.basicConfig(level=logging.INFO)

async def main():
    sup = Bot(token=tbt,parse_mode="HTML")
    dp = Dispatcher()

    dp.include_routers(questions.router,admin.router)

    await sup.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(sup)

    print('Бот запущен')
if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Bye-bye')
        exit()