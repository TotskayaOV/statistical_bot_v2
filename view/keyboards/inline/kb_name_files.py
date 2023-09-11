from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from view.callback import files_name

kb_files_name = InlineKeyboardMarkup(row_width=3)

btn_sla = InlineKeyboardButton(text='Jira SLA', callback_data=files_name.new(file_name='file_jsla'))
btn_time = InlineKeyboardButton(text='Jira Time', callback_data=files_name.new(file_name='file_jtime'))
btn_count = InlineKeyboardButton(text='Jira count', callback_data=files_name.new(file_name='file_jcount'))
btn_portal = InlineKeyboardButton(text='Портал', callback_data=files_name.new(file_name='file_portal'))
btn_call = InlineKeyboardButton(text='Звонки', callback_data=files_name.new(file_name='file_call'))
btn_back = InlineKeyboardButton(text='Назад', callback_data=files_name.new(file_name='file_back'))

kb_files_name.add(btn_sla, btn_time, btn_count)
kb_files_name.add(btn_portal, btn_call)
kb_files_name.add(btn_back)
