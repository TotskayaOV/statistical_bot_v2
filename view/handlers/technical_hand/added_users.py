from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext

from loader import dp, user_db
from view.states import NewUser
from view.callback import users_status, button_cancel, technik_menu_31
from view.keyboards.inline import kb_cancel_fsm, create_kb_user_status, kb_tech_lev21
from controller import added_users_from_db, get_name_user_data_to_str


@dp.callback_query_handler(technik_menu_31.filter(level_t31='add_user_data2'))
async def add_new_user(call: CallbackQuery, admin: bool):
    """
    Переход в state добавления пользователя
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        users_list = get_name_user_data_to_str()
        await dp.bot.edit_message_text(text=f'Переход в режим добавления нового пользователя.\n\n{users_list}\n\n'
                                            f'<b>Введите фамилию</b>', chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_cancel_fsm, parse_mode=ParseMode.HTML)
        await NewUser.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=NewUser.user_name, content_types=ContentTypes.ANY)
async def write_user_name(message: Message, state: FSMContext):
    users_input = message.text
    users_input = users_input.capitalize()
    await state.update_data({'user_name': users_input.capitalize()})
    await message.answer(text='Задайте статус пользователя\n<i>Статус "деактивирован" не позволяет пользователю'
                              'запрашивать у бота данные</i>',
                         parse_mode=ParseMode.HTML, reply_markup=create_kb_user_status())
    await NewUser.next()


@dp.callback_query_handler(users_status.filter(u_status='admin_add'), state=NewUser.user_status)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'user_status': 'admin'})
    data = await state.get_data()
    if added_users_from_db(data) is True:
        check_text = f'Пользователь {data.get("user_name")} в статусе <b>администратор</b> добавлен 👍'
    else:
        check_text = f'Произошёл сбой! Пользователь {data.get("user_name")} не добавлен 👎'
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'{check_text}\n__________________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)


@dp.callback_query_handler(users_status.filter(u_status='coor_add'), state=NewUser.user_status)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'user_status': 'coordinator'})
    data = await state.get_data()
    if added_users_from_db(data) is True:
        check_text = f'Пользователь {data.get("user_name")} в статусе <b>координатор</b> добавлен 👍'
    else:
        check_text = f'Произошёл сбой! Пользователь {data.get("user_name")} не добавлен 👎'
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'{check_text}\n__________________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)


@dp.callback_query_handler(users_status.filter(u_status='deact_add'), state=NewUser.user_status)
async def finish_added2(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'user_status': 'deactivate'})
    data = await state.get_data()
    added_users_from_db(data)
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)
