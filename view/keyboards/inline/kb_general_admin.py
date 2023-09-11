from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import general_menu

kb_general_admin_menu = InlineKeyboardMarkup(row_width=2)

btn_admin = InlineKeyboardButton(text='Администратор', callback_data=general_menu.new(level1='admin_1'))
btn_tech = InlineKeyboardButton(text='Техник', callback_data=general_menu.new(level1='tech_1'))

kb_general_admin_menu.row(btn_admin, btn_tech)