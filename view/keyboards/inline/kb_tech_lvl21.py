from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_21, general_menu

kb_tech_lev21 = InlineKeyboardMarkup(row_width=3)

btn_add = InlineKeyboardButton(text='Добавить', callback_data=technik_menu_21.new(level_t21='add_user_data'))
btn_edit = InlineKeyboardButton(text='Редактировать', callback_data=technik_menu_21.new(level_t21='edit_user_data'))
btn_del = InlineKeyboardButton(text='Удалить', callback_data=technik_menu_21.new(level_t21='del_user_data'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=general_menu.new(level1='tech_1'))

kb_tech_lev21.add(btn_add, btn_edit, btn_del)
kb_tech_lev21.add(btn_back)
