from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_33, technik_menu_1

kb_tech_lev33 = InlineKeyboardMarkup(row_width=3)

btn_edit_us = InlineKeyboardButton(text='Пользователь', callback_data=technik_menu_33.new(level_t33='edit_user_data2'))
btn_edit_tg = InlineKeyboardButton(text='ID Телеграмма', callback_data=technik_menu_33.new(level_t33='edit_tg_data'))
btn_edit_st = InlineKeyboardButton(text='Статус', callback_data=technik_menu_33.new(level_t33='edit_status'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=technik_menu_1.new(level_t1='users'))

kb_tech_lev33.add(btn_edit_us, btn_edit_tg, btn_edit_st)
kb_tech_lev33.add(btn_back)