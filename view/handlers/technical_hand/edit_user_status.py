from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext

from loader import dp, user_db
from view.states import EditUserStatus
from view.callback import users_status, button_cancel, technik_menu_41
from view.keyboards.inline import kb_cancel_fsm, create_kb_user_status, kb_tech_lev21
from controller import update_user_data_from_db, get_name_user_data_to_str


@dp.callback_query_handler(technik_menu_41.filter(level_t41='edit_user_st'))
async def add_new_user(call: CallbackQuery, admin: bool):
    """
    Переход в state изменения статуса пользователя
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    us_list = get_name_user_data_to_str()
    if admin:
        await dp.bot.edit_message_text(text=f'Переход в режим изменения статуса пользователя.\n'
                                            f'{us_list}\n Введите <b>ID пользователя</b> из списка 👆',
                                       chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_cancel_fsm, parse_mode=ParseMode.HTML)
        await EditUserStatus.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=EditUserStatus.user_id, content_types=ContentTypes.ANY)
async def write_user_id(message: Message, state: FSMContext):
    users_input = message.text
    try:
        users_input = int(users_input)
        await state.update_data({'user_id': users_input})
        await message.answer(text='Выберите статус пользователя',
                             parse_mode=ParseMode.HTML, reply_markup=create_kb_user_status(new=False))
        await EditUserStatus.next()
    except:
        await message.answer(text='Ошибка ввода. Введите <b>ID пользователя</b> из списка. ТОЛЬКО ЦИФРЫ ',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await EditUserStatus.user_id.set()


@dp.callback_query_handler(users_status.filter(u_status='admin_ed'), state=EditUserStatus.user_status)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'user_status': 'admin'})
    data = await state.get_data()
    update_user_data_from_db('user status', data)
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Cтатус изменен на <b>администратор</b>👍\n_______________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)


@dp.callback_query_handler(users_status.filter(u_status='coor_ed'), state=EditUserStatus.user_status)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'user_status': 'coordinator'})
    data = await state.get_data()
    update_user_data_from_db('user status', data)
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Cтатус изменен на <b>координатор</b> 👍\n________________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)


@dp.callback_query_handler(users_status.filter(u_status='deact_ed'), state=EditUserStatus.user_status)
async def finish_added2(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'user_status': 'deactivate'})
    data = await state.get_data()
    update_user_data_from_db('user status', data)
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Пользователь деактивирован 👌\n__________________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)
