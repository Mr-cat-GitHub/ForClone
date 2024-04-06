from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove
from aiogram.utils.keyboard import ReplyKeyboardBuilder

start_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Меню"),
            KeyboardButton(text="FAQ")
        ],
        [
            KeyboardButton(text="Длинная херня для теста этого"),
            KeyboardButton(text="Доставка")
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует??!'
)


del_kbd = ReplyKeyboardRemove()


test_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="FAQ"),
        ],
        [
            KeyboardButton(text="Отправить номер", request_contact=True),
            KeyboardButton(text="Отправить локацию", request_location=True)
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder='Что вас интересует??!'
)


start_kb2 = ReplyKeyboardBuilder()
start_kb2.add(
    KeyboardButton(text="Длинная херня для теста этого"),
    KeyboardButton(text="Доставка"),
    KeyboardButton(text="Меню"),
    KeyboardButton(text="FAQ")
)
start_kb2.adjust(2, 2)


start_kb3 = ReplyKeyboardBuilder()
start_kb3.attach(start_kb2)
start_kb3.row(KeyboardButton(text="LOL"))

start_kb3.adjust(2, 2, 1)
