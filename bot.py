from config_data.config import load_config, Config
from aiogram import Dispatcher, Bot
import logging
import asyncio
from keyboards.main_menu import set_main_menu
from handlers import user_handlers, other_msg

async def main():
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s')
    logging.info('Starting bot')
    
    config: Config = load_config()
    bot: Bot = Bot(config.tgbot.token, parse_mode='HTML')
    dp: Dispatcher = Dispatcher()
    
    dp.include_router(user_handlers.router)
    dp.include_router(other_msg.router)
    await set_main_menu(bot)
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())