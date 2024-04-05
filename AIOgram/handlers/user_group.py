from string import punctuation

from aiogram import types, Router

from filters.chat_types import ChatTypeFilter

user_group_router = Router()
user_group_router.message.filter(ChatTypeFilter(["group", "supergroup"]))

restricted_words = {"хохля", "pon", "пон"}


def clear_text(text: str):
    return text.translate(str.maketrans("", "", punctuation))


@user_group_router.edited_message()
@user_group_router.message()
async def cleaner(message: types.Message):
    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f"Restricted word, @{message.from_user.username}. Чепушила")
        await message.delete()

