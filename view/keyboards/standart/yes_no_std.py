from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from .cancel import btn_cancel

kb_yes_no_std = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_yes = KeyboardButton(text='Да')
btn_no = KeyboardButton(text='Нет')

kb_yes_no_std.add(btn_yes, btn_no)
kb_yes_no_std.add(btn_cancel)
