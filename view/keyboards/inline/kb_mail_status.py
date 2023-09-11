from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import mail_status, button_cancel


kb_mail_status = InlineKeyboardMarkup(row_width=2)
btn_cancel = InlineKeyboardButton(text='Отмена', callback_data=button_cancel.new(cansel_fsm='cancel_fsm'))
btn_activ = InlineKeyboardButton(text='активировать', callback_data=mail_status.new(m_status='mail_activ'))
btn_deact = InlineKeyboardButton(text='деактивировать', callback_data=mail_status.new(m_status='mail_deactiv'))

kb_mail_status.add(btn_activ, btn_deact)
kb_mail_status.add(btn_cancel)
