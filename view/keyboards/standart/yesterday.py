from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from datetime import datetime, timedelta
from .cancel import btn_cancel


kb_yesterday = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)

btn_yesterday = KeyboardButton(text=str(datetime.now().date()- timedelta(days=1)))

kb_yesterday.add(btn_yesterday, btn_cancel)