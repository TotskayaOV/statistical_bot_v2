from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_35, technik_menu_1

kb_tech_lev35 = InlineKeyboardMarkup(row_width=3)

btn_del_sla = InlineKeyboardButton(text='Jira SLA', callback_data=technik_menu_35.new(level_t35='del_jsla'))
btn_del_time = InlineKeyboardButton(text='Jira Time', callback_data=technik_menu_35.new(level_t35='del_jtime'))
btn_del_count = InlineKeyboardButton(text='Jira count', callback_data=technik_menu_35.new(level_t35='del_jcount'))
btn_del_portal = InlineKeyboardButton(text='Портал', callback_data=technik_menu_35.new(level_t35='del_portal'))
btn_del_general = InlineKeyboardButton(text='Общие данные', callback_data=technik_menu_35.new(level_t35='del_general'))
btn_del_call = InlineKeyboardButton(text='Звонки', callback_data=technik_menu_35.new(level_t35='del_call'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=technik_menu_1.new(level_t1='all_data'))

kb_tech_lev35.add(btn_del_sla, btn_del_time, btn_del_count)
kb_tech_lev35.add(btn_del_call, btn_del_portal, btn_del_general)
kb_tech_lev35.add(btn_back)