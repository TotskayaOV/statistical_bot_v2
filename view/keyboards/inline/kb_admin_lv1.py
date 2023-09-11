from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import admin_menu_1

kb_admin_lev1 = InlineKeyboardMarkup(row_width=2)

btn_verif_speed = InlineKeyboardButton(text='Скорость', callback_data=admin_menu_1.new(level_a1='speed'))
btn_perfom = InlineKeyboardButton(text='Производительность', callback_data=admin_menu_1.new(level_a1='perfom'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=admin_menu_1.new(level_a1='back_gen'))

kb_admin_lev1.add(btn_verif_speed, btn_perfom)
kb_admin_lev1.add(btn_back)
