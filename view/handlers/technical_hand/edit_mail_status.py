from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext

from loader import dp, user_db
from view.states import EditMail
from view.callback import mail_status, button_cancel, technik_menu_41
from view.keyboards.inline import kb_cancel_fsm, kb_mail_status, kb_tech_lev21
from controller import update_user_data_from_db, get_tg_user_data_to_str


@dp.callback_query_handler(technik_menu_41.filter(level_t41='edit_tg_st'))
async def edit_mail_user(call: CallbackQuery, admin: bool):
    """
    Переход в state изменения статуса рассылки
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    us_list = get_tg_user_data_to_str()
    if admin:
        await dp.bot.edit_message_text(text=f'Переход в режим изменения статуса рассылки пользователю.\n'
                                            f'{us_list}\n Введите <b>ID пользователя</b> из списка 👆',
                                       chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_cancel_fsm, parse_mode=ParseMode.HTML)
        await EditMail.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=EditMail.user_id, content_types=ContentTypes.ANY)
async def write_user_id(message: Message, state: FSMContext):
    users_input = message.text
    try:
        users_input = int(users_input)
        await state.update_data({'user_id': users_input})
        await message.answer(text='Выберите статус рассылки:\n<b>активировать</b> - пользователь первым написал боту '
                                  'и может получать рассылку от администраторов\n<b>деактивировать</b> - пользователь '
                                  'не писал боту или залокировал его. Пользователь будет исключен из общей '
                                  'рассылки от администраторов (внимание! данный статус не ограничивает доступ '
                                  'пользователя к функционалу бота',
                             parse_mode=ParseMode.HTML, reply_markup=kb_mail_status)
        await EditMail.next()
    except:
        await message.answer(text='Ошибка ввода. Введите <b>ID пользователя</b> из списка. ТОЛЬКО ЦИФРЫ ',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await EditMail.user_id.set()


@dp.callback_query_handler(mail_status.filter(m_status='mail_activ'), state=EditMail.mail_status)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'mail_status': 1})
    data = await state.get_data()
    update_user_data_from_db('mail status', data)
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Теперь пользователь может получить от тебя привет 🤗\n'
                                        f'__________________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)


@dp.callback_query_handler(mail_status.filter(m_status='mail_deactiv'), state=EditMail.mail_status)
async def finish_added(call: CallbackQuery, state: FSMContext):
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await state.update_data({'mail_status': 0})
    data = await state.get_data()
    update_user_data_from_db('mail status', data)
    await state.reset_data()
    await state.finish()
    await dp.bot.edit_message_text(text=f'Теперь пользователь не будет получать сообщения от бота 🥲\n'
                                        f'__________________________________\n\n'
                                        f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)

