from aiogram import types, Router, F
from aiogram.filters import CommandStart, Command, or_f
from filters.chat_types import ChatTypeFilter
from kbds import reply

user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(["private"]))


@user_private_router.message(CommandStart())
async def start_greet(message: types.Message):
    print(message.text)
    await message.answer(f"Привет {message.from_user.first_name}, я виртуальный помощник:", reply_markup=reply.start_kb3.as_markup(
        resize_keyboard=True,
        input_field_placeholder="Что вас интересует?"
    )) # или это можно сделать так:
    # await message.answer(f"Привет {message.from_user.first_name}, я виртуальный помощник:", reply_markup=reply.start_kb)


# @user_private_router.message((F.text.lower().contains("menu")) | (F.text.lower().contains("мен")))
@user_private_router.message(or_f(Command("menu"), (F.text.lower().contains("menu")) | (F.text.lower().contains("мен"))))
async def menu_cmd(message: types.Message):
    print(message.text)
    await message.answer("Меню: ")


@user_private_router.message((F.text.lower().contains("help")) | (F.text.lower().contains("faq")))
@user_private_router.message(Command("help"))
async def help_cmd(message: types.Message):
    await message.answer("""<b>Список команд бота:</b>
                        \n/start - обновление/запуск бота
                        \n/menu - вывод меню
                        \n/test - developer test """)


@user_private_router.message(F.text.lower().contains("доставк"))
@user_private_router.message(Command("delivery"))
async def delivery_cmd(message: types.Message):
    await message.answer("Доставка по всем городам России")


@user_private_router.message(F.contact)
async def get_contact(message: types.Message):
    await message.answer(f"Спасибо {message.from_user.first_name}, номер получен")
    await message.answer(str(message.contact))


@user_private_router.message(F.location)
async def get_location(message: types.Message):
    await message.answer(f"Спасибо {message.from_user.first_name}, локация получена")
    await message.answer(str(message.location))


@user_private_router.message(Command("test"))
async def test_cmd(message: types.Message):

    await message.answer("<b>successful test</b>", reply_markup=reply.test_kb)
    await message.answer("LOL"
                         "\nAnon"
                         "\nХохля")
