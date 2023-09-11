from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import admin_menu_1, admin_menu_32

kb_admin_lev32 = InlineKeyboardMarkup(row_width=3)

btn_time = InlineKeyboardButton(text='Время', callback_data=admin_menu_32.new(level_a32='jira_time'))
btn_sla = InlineKeyboardButton(text='SLA', callback_data=admin_menu_32.new(level_a32='jira_sla'))
btn_count = InlineKeyboardButton(text='Количество', callback_data=admin_menu_32.new(level_a32='jira_count'))
btn_back2 = InlineKeyboardButton(text='Назад', callback_data=admin_menu_1.new(level_a1='perfom'))

kb_admin_lev32.row(btn_time, btn_sla, btn_count)
kb_admin_lev32.add(btn_back2)