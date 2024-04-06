from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode

from common.bot_cmds_list import private
from handlers.user_private import user_private_router
from handlers.user_group import user_group_router

import asyncio


bot = Bot(token="token", parse_mode=ParseMode.HTML)
dp = Dispatcher()
ALLOWED_UPDATES = ['message', 'edited_message']
dp.include_router(user_private_router)
dp.include_router(user_group_router)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    # await bot.delete_my_commands(scope=types.BotCommandScopeAllPrivateChats())
    await bot.set_my_commands(commands=private, scope=types.BotCommandScopeAllPrivateChats())
    await dp.start_polling(bot, allowed_updates=ALLOWED_UPDATES)


asyncio.run(main())
