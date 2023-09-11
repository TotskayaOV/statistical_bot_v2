from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_32, technik_menu_1

kb_tech_lev32 = InlineKeyboardMarkup(row_width=2)

btn_del_us = InlineKeyboardButton(text='Пользователь', callback_data=technik_menu_32.new(level_t32='del_user_data2'))
btn_del_tg = InlineKeyboardButton(text='id Телеграмма', callback_data=technik_menu_32.new(level_t32='del_tg_data'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=technik_menu_1.new(level_t1='users'))

kb_tech_lev32.add(btn_del_us, btn_del_tg)
kb_tech_lev32.add(btn_back)
