from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import technik_menu_41, technik_menu_21

kb_tech_lev41 = InlineKeyboardMarkup(row_width=2)

btn_edit_stu = InlineKeyboardButton(text='Статус\nпользователя',
                                    callback_data=technik_menu_41.new(level_t41='edit_user_st'))
btn_edit_sttg = InlineKeyboardButton(text='Статус\nрассылки',
                                     callback_data=technik_menu_41.new(level_t41='edit_tg_st'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=technik_menu_21.new(level_t21='edit_user_data'))

kb_tech_lev41.add(btn_edit_stu, btn_edit_sttg)
kb_tech_lev41.add(btn_back)