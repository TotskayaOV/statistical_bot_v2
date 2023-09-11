from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from aiogram.dispatcher import FSMContext

from loader import dp, user_db
from view.states import NewTgID
from view.callback import users_status, button_cancel, technik_menu_31
from view.keyboards.inline import kb_cancel_fsm, create_kb_user_status, kb_tech_lev21
from controller import get_name_user_data_to_str, added_tg_id_from_db


@dp.callback_query_handler(technik_menu_31.filter(level_t31='add_tg_data'))
async def add_new_user(call: CallbackQuery, admin: bool):
    """
    Переход в state добавления ID телеграма
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    us_list = get_name_user_data_to_str()
    if admin:
        await dp.bot.edit_message_text(text=f'Переход в режим добавления нового телеграмм ID пользователя.\n'
                                            f'{us_list}\n Введите <b>ID пользователя</b> из списка 👆',
                                       chat_id=user_id, message_id=current_msg,
                                       reply_markup=kb_cancel_fsm, parse_mode=ParseMode.HTML)
        await NewTgID.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=NewTgID.user_id, content_types=ContentTypes.ANY)
async def write_user_id(message: Message, state: FSMContext):
    users_input = message.text
    try:
        users_input = int(users_input)
        await state.update_data({'user_id': users_input})
        await message.answer(text='Введите <b>id телеграмма</b> пользователя',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await NewTgID.next()
    except:
        await message.answer(text='Ошибка ввода. Введите <b>ID пользователя</b> из списка. ТОЛЬКО ЦИФРЫ ',
                             parse_mode=ParseMode.HTML, reply_markup=kb_cancel_fsm)
        await NewTgID.user_id.set()


@dp.message_handler(state=NewTgID.tg_id, content_types=ContentTypes.ANY)
async def write_tg_id(message: Message, state: FSMContext):
    users_input = message.text
    try:
        users_input = int(users_input)
        await state.update_data({'tg_id': users_input})
        data = await state.get_data()
        if added_tg_id_from_db(data) is True:
            check_text = f'Телеграмм с id {data.get("tg_id")} добавлен 👍'
        else:
            check_text = f'Произошёл сбой! Телеграмм с id {data.get("tg_id")} не добавлен 👎'
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
        await NewTgID.tg_id.set()
