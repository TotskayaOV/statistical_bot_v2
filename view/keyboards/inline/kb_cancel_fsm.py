from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import button_cancel

kb_cancel_fsm = InlineKeyboardMarkup(row_width=1)

btn_cancel = InlineKeyboardButton(text='Отмена', callback_data=button_cancel.new(cansel_fsm='cancel_fsm'))

kb_cancel_fsm.row(btn_cancel)
