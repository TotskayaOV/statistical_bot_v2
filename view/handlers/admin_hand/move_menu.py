from aiogram.types import CallbackQuery, InputMediaPhoto, InputFile, ParseMode

from loader import dp
from view.keyboards.inline import kb_admin_lev1, kb_general_admin_menu, kb_admin_lev21, \
    kb_admin_lev22, kb_admin_lev31,kb_admin_lev32
from view.callback import admin_menu_1, general_menu, admin_menu_21, admin_menu_22, admin_menu_32


@dp.callback_query_handler(admin_menu_1.filter(level_a1='back_gen'))
async def back_general_admin_menu(call: CallbackQuery):
    """
    Возврат в генеральное меню администратора
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Привет, {user_name}!\nВыбери за кого будешь рулить 😎',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_general_admin_menu)


@dp.callback_query_handler(general_menu.filter(level1='admin_1'))
async def move_1lvl_admin(call: CallbackQuery):
    """
    Админ меню. L1
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Выбери какой вид отчета ты хочешь получить:\nДинамический отчет скорости'
                                        f' проверки или постоянные данные производительности отдела 🥸',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_admin_lev1)


@dp.callback_query_handler(admin_menu_1.filter(level_a1='perfom'))
async def check_upload_data(call: CallbackQuery):
    """
    Админ меню. L21
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Из какого источника будут загружаться данные?\n\n'
                                     f'<i>для загрузки общих данных по новым партнерам и проверки '
                                     f'за 15 минут выбери "Портал"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_admin_lev21)


@dp.callback_query_handler(admin_menu_1.filter(level_a1='speed'))
async def check_upload_report(call: CallbackQuery):
    """
    Админ меню. L22
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await dp.bot.edit_message_text(text=f'Какой отчет нужен?\nотчет <b>по дням</b> - будут показаны медиана и среднее '
                                     f'арифметическое по скорости проверки анкет разделенное по дням в файле, '
                                     f'\n<b>общий</b> отчет - будет посчитана общая медиана и среднее'
                                     f' арифметическое всех проверок. В последнем случае идентификаторы анкет будут '
                                     f'выгружены в файле .xlxs с дельтой времени',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_admin_lev22)


@dp.callback_query_handler(admin_menu_21.filter(level_a21='portal'))
async def check_upload_portal(call: CallbackQuery):
    """
    Админ меню. L31
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await dp.bot.edit_message_text(text=f'Будем загружать общие показатели или файл с данными с портала? 📥',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_admin_lev31)


@dp.callback_query_handler(admin_menu_21.filter(level_a21='jira'))
async def check_upload_jira(call: CallbackQuery):
    """
    Админ меню. L32
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await dp.bot.edit_message_text(text=f'Какие показатели Jira будем загружать? 📥',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_admin_lev32)
