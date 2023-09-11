from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import users_status, button_cancel


def create_kb_user_status(new=True):
    """
    Формирует клавиатуру статусов пользователей
    :param new: True - новый пользователь
                False - редактирование статуса
    :return: kb_object
    """
    kb_us_status = InlineKeyboardMarkup(row_width=2)
    btn_cancel = InlineKeyboardButton(text='Отмена', callback_data=button_cancel.new(cansel_fsm='cancel_fsm'))
    if new is True:
        btn_coor = InlineKeyboardButton(text='Координатор', callback_data=users_status.new(u_status='coor_add'))
        btn_admin = InlineKeyboardButton(text='Администратор', callback_data=users_status.new(u_status='admin_add'))
        btn_deact = InlineKeyboardButton(text='деактивирован', callback_data=users_status.new(u_status='deact_add'))
    else:
        btn_coor = InlineKeyboardButton(text='Координатор', callback_data=users_status.new(u_status='coor_ed'))
        btn_admin = InlineKeyboardButton(text='Администратор', callback_data=users_status.new(u_status='admin_ed'))
        btn_deact = InlineKeyboardButton(text='деактивирован', callback_data=users_status.new(u_status='deact_ed'))
    kb_us_status.add(btn_coor, btn_admin)
    kb_us_status.add(btn_deact, btn_cancel)
    return kb_us_status
