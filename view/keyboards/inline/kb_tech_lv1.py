from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_1, admin_menu_1

kb_tech_lev1 = InlineKeyboardMarkup(row_width=3)

btn_users = InlineKeyboardButton(text='Пользователи', callback_data=technik_menu_1.new(level_t1='users'))
btn_param_f = InlineKeyboardButton(text='Параметры', callback_data=technik_menu_1.new(level_t1='param_files'))
btn_download = InlineKeyboardButton(text='Данные', callback_data=technik_menu_1.new(level_t1='all_data'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=admin_menu_1.new(level_a1='back_gen'))

kb_tech_lev1.add(btn_users, btn_param_f, btn_download)
kb_tech_lev1.add(btn_back)
