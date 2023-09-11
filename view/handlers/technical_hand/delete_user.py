from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext

from loader import dp, user_db
from view.states import DelUser
from view.callback import users_status, button_cancel, technik_menu_32
from view.keyboards.inline import kb_cancel_fsm, create_kb_user_status, kb_tech_lev21
from controller import added_users_from_db, get_name_user_data_to_str


@dp.callback_query_handler(technik_menu_32.filter(level_t32='del_user_data2'))
async def del_user(call: CallbackQuery, admin: bool):
    """
    Переход в state удаления пользователя
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        users_list = get_name_user_data_to_str()
        await dp.bot.edit_message_text(text=f'Переход в режим удаления пользователя.\n\n{users_list}\n\n'
                                            f'<b>Введите id пользователя</b>', chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_cancel_fsm, parse_mode=ParseMode.HTML)
        await DelUser.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=DelUser.user_id, content_types=ContentTypes.ANY)
async def del_user_id(message: Message, state: FSMContext):
    users_input = message.text
    users_input = users_input.capitalize()
    try:
        users_input = int(users_input)
        await state.update_data({'user_id': users_input})
        await message.answer(text='Кнопка в разработке.\n____________________\n\n'
                                  'Выберите добавить нового пользователя или его id телеграмма, удалить '
                                  'пользователя или его id телеграмма, редактировать данные пользователя '
                                  '(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                  'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                  'во вкладку "Добавить" или "Редактировать"</i>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_tech_lev21)
        await state.reset_data()
        await state.finish()
    except:
        await message.answer(text='Ошибка ввода. Введите <b>ID пользователя</b> из списка. ТОЛЬКО ЦИФРЫ ',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await DelUser.user_id.set()
