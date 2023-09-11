from datetime import datetime

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import date_return


def kb_daily_report(date_str, step=True):
    kb_user_inline = InlineKeyboardMarkup(row_width=2)
    date_obj = datetime.strptime(date_str, '%Y-%m-%d')
    formatted_date = date_obj.strftime('%d.%m.%y')

    btn_one = InlineKeyboardButton(text=f'Назад к {formatted_date}',
                                   callback_data=date_return.new(button='one_day', date_obj=date_str))
    btn_period = InlineKeyboardButton(text='Данные за период',
                                      callback_data=date_return.new(button='period', date_obj=date_str))
    if step:
        return kb_user_inline.row(btn_period)
    else:
        return kb_user_inline.row(btn_one)