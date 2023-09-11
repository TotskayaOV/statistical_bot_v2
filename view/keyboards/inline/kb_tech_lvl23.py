from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_23, general_menu

kb_tech_lev23 = InlineKeyboardMarkup(row_width=3)

btn_delimiters = InlineKeyboardButton(text='Разделитель', callback_data=technik_menu_23.new(level_t23='delimiters'))
btn_datetime = InlineKeyboardButton(text='Время', callback_data=technik_menu_23.new(level_t23='datetime'))
btn_numstr = InlineKeyboardButton(text='№ строки', callback_data=technik_menu_23.new(level_t23='numstr'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=general_menu.new(level1='tech_1'))

kb_tech_lev23.add(btn_delimiters, btn_datetime, btn_numstr)
kb_tech_lev23.add(btn_back)