from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import admin_menu_21, general_menu

kb_admin_lev21 = InlineKeyboardMarkup(row_width=3)

btn_portal = InlineKeyboardButton(text='Портал', callback_data=admin_menu_21.new(level_a21='portal'))
btn_calls = InlineKeyboardButton(text='Звонки', callback_data=admin_menu_21.new(level_a21='calls'))
btn_jira = InlineKeyboardButton(text='Jira', callback_data=admin_menu_21.new(level_a21='jira'))
btn_back1 = InlineKeyboardButton(text='Назад', callback_data=general_menu.new(level1='admin_1'))

kb_admin_lev21.row(btn_portal, btn_calls, btn_jira)
kb_admin_lev21.add(btn_back1)