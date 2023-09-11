from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import general_menu

kb_general_user_menu = InlineKeyboardMarkup(row_width=2)

btn_stat_us = InlineKeyboardButton(text='Статистика за день', callback_data=general_menu.new(level1='user_stat'))
btn_help_us = InlineKeyboardButton(text='Помощь', callback_data=general_menu.new(level1='user_help'))

kb_general_user_menu.row(btn_stat_us, btn_help_us)