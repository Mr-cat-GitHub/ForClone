from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_greet(message: types.Message):
    print(message.text)
    await message.answer("Lol")


# @user_private_router.message((F.text.lower().contains("menu")) | (F.text.lower().contains("мен")))
@user_private_router.message(or_f(Command("menu"), (F.text.lower().contains("menu")) | (F.text.lower().contains("мен"))))
async def menu_cmd(message: types.Message):
    print(message.text)
    await message.answer("Меню: ")


@user_private_router.message((F.text.lower().contains("help")) | (F.text.lower().contains("faq")))
@user_private_router.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("""**Список команд бота:**
                        \n/start - обновление/запуск бота
                        \n/menu - вывод меню""")
