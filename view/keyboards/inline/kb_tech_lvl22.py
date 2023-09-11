from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_22, general_menu

kb_tech_lev22 = InlineKeyboardMarkup(row_width=2)

btn_download = InlineKeyboardButton(text='Скачать', callback_data=technik_menu_22.new(level_t22='download_data'))
btn_delete = InlineKeyboardButton(text='Удалить', callback_data=technik_menu_22.new(level_t22='delete_data'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=general_menu.new(level1='tech_1'))

kb_tech_lev22.add(btn_download, btn_delete)
kb_tech_lev22.add(btn_back)
