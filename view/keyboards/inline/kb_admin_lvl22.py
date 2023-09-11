from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import admin_menu_22, general_menu

kb_admin_lev22 = InlineKeyboardMarkup(row_width=2)

btn_days = InlineKeyboardButton(text='по дням', callback_data=admin_menu_22.new(level_a22='days'))
btn_times = InlineKeyboardButton(text='общее', callback_data=admin_menu_22.new(level_a22='times'))
btn_back1 = InlineKeyboardButton(text='Назад', callback_data=general_menu.new(level1='admin_1'))

kb_admin_lev22.row(btn_days, btn_times)
kb_admin_lev22.add(btn_back1)