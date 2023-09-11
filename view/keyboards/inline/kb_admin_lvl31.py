from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import admin_menu_1, admin_menu_31

kb_admin_lev31 = InlineKeyboardMarkup(row_width=3)

btn_all_data = InlineKeyboardButton(text='Общие данные', callback_data=admin_menu_31.new(level_a31='all_data'))
btn_portal_file = InlineKeyboardButton(text='Проверка', callback_data=admin_menu_31.new(level_a31='portal_file'))
btn_back2 = InlineKeyboardButton(text='Назад', callback_data=admin_menu_1.new(level_a1='perfom'))

kb_admin_lev31.row(btn_all_data , btn_portal_file)
kb_admin_lev31.add(btn_back2)