from aiogram.types import CallbackQuery, ParseMode, ContentTypes, Message
from aiogram.dispatcher import FSMContext

from loader import dp
from view.keyboards.inline import kb_files_name, kb_cancel_fsm, kb_tech_lev23
from view.callback import files_name, technik_menu_23
from view.states import NewNumStr
from controller import get_params_file, updating_data_for_parsing


@dp.callback_query_handler(technik_menu_23.filter(level_t23='numstr'))
async def add_new_user(call: CallbackQuery, admin: bool):
    """
    Переход в state изменения № строки в файле
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    datetime_list = get_params_file('numbers_start_row')
    if admin:
        await dp.bot.edit_message_text(text=f'Переход в режим изменения начала чтения в загружаемых файлах.\n'
                                            f'{datetime_list}\n Выберите файл',
                                       chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_files_name, parse_mode=ParseMode.HTML)
        await NewNumStr.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(files_name.filter(file_name='file_jsla'), state=NewNumStr.name_file)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'name_file': 'sla'})
    await dp.bot.edit_message_text(text=f'Введите новый номер строки для начала чтения файла Jira SLA',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_cancel_fsm)
    await NewNumStr.next()


@dp.callback_query_handler(files_name.filter(file_name='file_jtime'), state=NewNumStr.name_file)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'name_file': 'time'})
    await dp.bot.edit_message_text(text=f'Введите новый номер строки для начала чтения файла Jira time',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_cancel_fsm)
    await NewNumStr.next()


@dp.callback_query_handler(files_name.filter(file_name='file_jcount'), state=NewNumStr.name_file)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'name_file': 'count'})
    await dp.bot.edit_message_text(text=f'Введите новый номер строки для начала чтения файла количества заявок Jira',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_cancel_fsm)
    await NewNumStr.next()


@dp.callback_query_handler(files_name.filter(file_name='file_portal'), state=NewNumStr.name_file)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'name_file': 'general_portal'})
    await dp.bot.edit_message_text(text=f'Введите новый номер строки для начала чтения файла проверки анкет на портале',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_cancel_fsm)
    await NewNumStr.next()


@dp.callback_query_handler(files_name.filter(file_name='file_call'), state=NewNumStr.name_file)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'name_file': 'call'})
    await dp.bot.edit_message_text(text=f'Введите новый номер строки для начала чтения файла количества звонков',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_cancel_fsm)
    await NewNumStr.next()


@dp.callback_query_handler(files_name.filter(file_name='file_back'), state=NewNumStr.name_file)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Для изменения параметров чтения файла, выберите параметр, далее название '
                                        f'файла и введите новое значение. При выборе названия файла будут выведены '
                                        f'текущие настройки чтения файла.',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev23)


@dp.message_handler(state=NewNumStr.new_value, content_types=ContentTypes.ANY)
async def write_user_id(message: Message, state: FSMContext):
    await state.update_data({'new_value': message.text})
    data = await state.get_data()
    data['name_table'] = 'num_row'
    updating_data_for_parsing(**data)
    await message.answer(text='Новый номер строки для начала чтения файла установлен\n\n'
                              'Для изменения параметров чтения файла, выберите параметр, далее название '
                              'файла и введите новое значение. При выборе названия файла будут выведены '
                              'текущие настройки чтения файла.',
                         parse_mode=ParseMode.HTML, reply_markup=kb_tech_lev23)
    await state.reset_data()
    await state.finish()
