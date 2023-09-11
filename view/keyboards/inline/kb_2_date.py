from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import menu_2_date
from .kb_cancel_fsm import btn_cancel

from datetime import datetime, timedelta

def kb_date(button_portal='file'):
    kb_date_menu = InlineKeyboardMarkup(row_width=2)
    date_yesterday = datetime.now().date() - timedelta(days=1)
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    if button_portal == 'file':
        btn_yesterday = InlineKeyboardButton(text=f'{str(date_yesterday)}',
                                             callback_data=menu_2_date.new(date_priority='yesterday'))
        btn_bf_yesterday = InlineKeyboardButton(text=f'{str(date_bf_yesterday)}',
                                            callback_data=menu_2_date.new(date_priority='bf_yesterday'))
    else:
        btn_yesterday = InlineKeyboardButton(text=f'{str(date_yesterday)}',
                                             callback_data=menu_2_date.new(date_priority='yesterday_general'))
        btn_bf_yesterday = InlineKeyboardButton(text=f'{str(date_bf_yesterday)}',
                                                callback_data=menu_2_date.new(date_priority='bf_yesterday_general'))
    kb_date_menu.row(btn_yesterday, btn_bf_yesterday)
    kb_date_menu.add(btn_cancel)
    return kb_date_menu