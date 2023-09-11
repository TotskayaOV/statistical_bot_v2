from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext

from loader import dp, user_db
from view.states import EditTgId
from view.callback import mail_status, button_cancel, technik_menu_33
from view.keyboards.inline import kb_cancel_fsm, kb_tech_lev21
from controller import update_user_data_from_db, get_tg_user_data_to_str


@dp.callback_query_handler(technik_menu_33.filter(level_t33='edit_tg_data'))
async def edit_tg_id(call: CallbackQuery, admin: bool):
    """
    Переход в state изменения ID телеграмма пользователя
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    us_list = get_tg_user_data_to_str()
    if admin:
        await dp.bot.edit_message_text(text=f'Переход в режим изменения ID телеграмма пользователя.\n'
                                            f'{us_list}\n Введите <b>ID пользователя</b> из списка 👆',
                                       chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_cancel_fsm, parse_mode=ParseMode.HTML)
        await EditTgId.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=EditTgId.user_id, content_types=ContentTypes.ANY)
async def write_user_id(message: Message, state: FSMContext):
    users_input = message.text
    try:
        users_input = int(users_input)
        await state.update_data({'user_id': users_input})
        await message.answer(text='Введите новый ID телеграма пользователя',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await EditTgId.next()
    except:
        await message.answer(text='Ошибка ввода. Введите <b>ID пользователя</b> из списка. ТОЛЬКО ЦИФРЫ ',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await EditTgId.user_id.set()


@dp.message_handler(state=EditTgId.tg_id, content_types=ContentTypes.ANY)
async def write_tg_id(message: Message, state: FSMContext):
    users_input = message.text
    try:
        users_input = int(users_input)
        await state.update_data({'tg_id': users_input})
        data = await state.get_data()
        update_user_data_from_db('tg id', data)
        check_text = f'Телеграмм ID изменен на id{data.get("tg_id")} 👍'
        await state.reset_data()
        await state.finish()
        await message.answer(text=f'{check_text}\n__________________________________\n\n'
                                  f'Выберите добавить нового пользователя или его id телеграмма, удалить '
                                  f'пользователя или его id телеграмма, редактировать данные пользователя '
                                  f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                  f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                  f'во вкладку "Добавить" или "Редактировать"</i>',
                             parse_mode=ParseMode.HTML, reply_markup=kb_tech_lev21)
    except:
        await message.answer(text='Ошибка ввода. Введите <b>телеграмм ID</b>. ТОЛЬКО ЦИФРЫ ',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await EditTgId.tg_id.set()
