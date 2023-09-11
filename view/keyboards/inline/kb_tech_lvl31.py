from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_31, technik_menu_1

kb_tech_lev31 = InlineKeyboardMarkup(row_width=2)

btn_add_us = InlineKeyboardButton(text='Пользователь', callback_data=technik_menu_31.new(level_t31='add_user_data2'))
btn_add_tg = InlineKeyboardButton(text='id Телеграмма', callback_data=technik_menu_31.new(level_t31='add_tg_data'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=technik_menu_1.new(level_t1='users'))

kb_tech_lev31.add(btn_add_us, btn_add_tg)
kb_tech_lev31.add(btn_back)
