import os
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from datetime import datetime, timedelta

from loader import dp
from view.keyboards.inline import kb_date, kb_tech_lev35, kb_cancel_fsm
from view.states import DelJiraSLA, DelJiraTime, DelJiraCount, DelPortal, DelGeneralData, DelCalls
from view.callback import technik_menu_35, menu_2_date
from controller import deleted_data_for_date


@dp.callback_query_handler(technik_menu_35.filter(level_t35='del_jsla'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления данных Jira SLA
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await DelJiraSLA.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=DelJiraSLA.date_data)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление Jira sla за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    deleted_data_for_date('j_sla', date_yesterday)
    await dp.bot.edit_message_text(text=f'Данные Jira SLA за {date_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=DelJiraSLA.date_data)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление Jira sla за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    deleted_data_for_date('j_sla', date_bf_yesterday)
    await dp.bot.edit_message_text(text=f'Данные Jira SLA за {date_bf_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.message_handler(state=DelJiraSLA.date_data, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и удаление Jira sla
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        DelJiraSLA.date_data.set()
    else:
        deleted_data_for_date('j_sla', data_obj)
        await message.answer(text=f'Данные Jira SLA за {data_obj} удалены.', reply_markup=kb_tech_lev35)
        await state.reset_data()
        await state.finish()


@dp.callback_query_handler(technik_menu_35.filter(level_t35='del_jtime'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления данных Jira Time
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await DelJiraTime.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=DelJiraTime.date_data)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление Jira time за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    deleted_data_for_date('j_time', date_yesterday)
    await dp.bot.edit_message_text(text=f'Данные Jira Time за {date_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=DelJiraTime.date_data)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление Jira time за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    deleted_data_for_date('j_time', date_bf_yesterday)
    await dp.bot.edit_message_text(text=f'Данные Jira Time за {date_bf_yesterday} удалены',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.message_handler(state=DelJiraTime.date_data, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и удаление Jira time
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        DelJiraTime.date_data.set()
    else:
        deleted_data_for_date('j_time', data_obj)
        await message.answer(text=f'Данные Jira Time за {data_obj} удалены.', reply_markup=kb_tech_lev35)
        await state.reset_data()
        await state.finish()


@dp.callback_query_handler(technik_menu_35.filter(level_t35='del_jcount'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления данных Jira count
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await DelJiraCount.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=DelJiraCount.date_data)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление Jira count за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    deleted_data_for_date('j_count', date_yesterday)
    await dp.bot.edit_message_text(text=f'Данные Jira count за {date_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=DelJiraCount.date_data)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление Jira count за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    deleted_data_for_date('j_count', date_bf_yesterday)
    await dp.bot.edit_message_text(text=f'Данные Jira count за {date_bf_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.message_handler(state=DelJiraCount.date_data, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и Удаление Jira count
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        DelJiraSLA.date_data.set()
    else:
        deleted_data_for_date('j_count', data_obj)
        await message.answer(text=f'Данные Jira count за {data_obj} удалены.', reply_markup=kb_tech_lev35)
        await state.reset_data()
        await state.finish()


@dp.callback_query_handler(technik_menu_35.filter(level_t35='del_portal'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления данных Портал
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await DelPortal.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=DelPortal.date_data)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление данных портала за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    deleted_data_for_date('portal', date_yesterday)
    await dp.bot.edit_message_text(text=f'Данные портала за {date_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=DelPortal.date_data)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление данных портала за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    deleted_data_for_date('portal', date_bf_yesterday)
    await dp.bot.edit_message_text(text=f'Данные портала за {date_bf_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.message_handler(state=DelPortal.date_data, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и удаление данных портала
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        DelJiraSLA.date_data.set()
    else:
        deleted_data_for_date('portal', data_obj)
        await message.answer(text=f'Данные портала за {data_obj} удалены.', reply_markup=kb_tech_lev35)
        await state.reset_data()
        await state.finish()


@dp.callback_query_handler(technik_menu_35.filter(level_t35='del_general'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления общих данных проверки
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await DelGeneralData.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=DelGeneralData.date_data)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление общих данных проверки за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    deleted_data_for_date('general', date_yesterday)
    await dp.bot.edit_message_text(text=f'Общие данные проверки за {date_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=DelGeneralData.date_data)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление общих данных проверки за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    deleted_data_for_date('general', date_bf_yesterday)
    await dp.bot.edit_message_text(text=f'Общие данные проверки за {date_bf_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.message_handler(state=DelGeneralData.date_data, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и удаление общих данных проверки
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        DelGeneralData.date_data.set()
    else:
        deleted_data_for_date('general', data_obj)
        await message.answer(text=f'Общие данные проверки за {data_obj} удалены.', reply_markup=kb_tech_lev35)
        await state.reset_data()
        await state.finish()


@dp.callback_query_handler(technik_menu_35.filter(level_t35='del_call'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления данных о звонках
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await DelCalls.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=DelCalls.date_data)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление данных о звонках за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    deleted_data_for_date('call', date_yesterday)
    await dp.bot.edit_message_text(text=f'Данные о звонках за {date_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=DelCalls.date_data)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Удаление данных о звонках за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_bf_yesterday = datetime.now().date() - timedelta(days=2)
    deleted_data_for_date('call', date_bf_yesterday)
    await dp.bot.edit_message_text(text=f'Данные о звонках за {date_bf_yesterday} удалены.',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev35,
                                   parse_mode=ParseMode.HTML)
    await state.reset_data()
    await state.finish()


@dp.message_handler(state=DelCalls.date_data, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и удаление данных о звонках
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        DelCalls.date_data.set()
    else:
        deleted_data_for_date('call', data_obj)
        await message.answer(text=f'Данные о звонках за {data_obj} удалены.', reply_markup=kb_tech_lev35)
        await state.reset_data()
        await state.finish()
