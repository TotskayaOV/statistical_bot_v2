from aiogram.types import CallbackQuery, InputMediaPhoto, InputFile, ParseMode

from loader import dp
from view.keyboards.inline import kb_tech_lev1, kb_tech_lev21, kb_tech_lev22, kb_tech_lev23, \
    kb_tech_lev31, kb_tech_lev32, kb_tech_lev33, kb_tech_lev35, \
    kb_tech_lev41
from view.callback import technik_menu_1, general_menu, technik_menu_21, technik_menu_22, \
    technik_menu_33


@dp.callback_query_handler(general_menu.filter(level1='tech_1'))
async def move_1lvl_tech(call: CallbackQuery):
    """
    Тех меню. L1
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Выбери с чем ты планируешь работать? 🥸',
                                   chat_id=user_id, message_id=current_msg, reply_markup=kb_tech_lev1)


@dp.callback_query_handler(technik_menu_1.filter(level_t1='users'))
async def update_users_data(call: CallbackQuery):
    """
    Тех меню. L21
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Выберите добавить нового пользователя или его id телеграмма, удалить'
                                        f'пользователя или его id телеграмма, редактировать данные пользователя '
                                        f'(имя, id телеграмма, статус пользователя или возможность доставки ему '
                                        f'отчетов)\n<i>Чтобы посмотреть список пользователей или их статус перейдите '
                                        f'во вкладку "Добавить" или "Редактировать"</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev21)


@dp.callback_query_handler(technik_menu_1.filter(level_t1='param_files'))
async def update_users_data(call: CallbackQuery):
    """
    Тех меню. L23
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await dp.bot.edit_message_text(text=f'Для изменения параметров чтения файла, выберите параметр, далее название '
                                        f'файла и введите новое значение. При выборе названия файла будут выведены '
                                        f'текущие настройки чтения файла.',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev23)


@dp.callback_query_handler(technik_menu_1.filter(level_t1='all_data'))
async def update_users_data(call: CallbackQuery):
    """
    Тех меню. L22
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    await dp.bot.edit_message_text(text=f'При ошибочной загрузке данных, есть возможность удалить загруженные данные. '
                                        f'Для того, чтобы скачать данные из базы данных потребуется ввод пароля.',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev22)


@dp.callback_query_handler(technik_menu_21.filter(level_t21='add_user_data'))
async def add_users_data(call: CallbackQuery):
    """
    Тех меню. L31
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Выберите что будем добавлять: нового пользователя или его id телеграмма.\n'
                                        f'<i>Нового пользователя необходимо добавить, чтобы его данные загружались в '
                                        f'базу данных и учитывались при расчете общих показателей отдела. '
                                        f'Отсутствие пользователя в базе данных не вызовет ошибки при загрузке '
                                        f'данных, но общие и средние показатели могут быть недостоверными.</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev31)


@dp.callback_query_handler(technik_menu_21.filter(level_t21='del_user_data'))
async def del_users_data(call: CallbackQuery):
    """
    Тех меню. L32
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Выберите что будем удалять: нового пользователя или его id телеграмма.\n'
                                        f'<i>Обрати внимание, что удаление пользователя из базы данных '
                                        f'повлечет за собой удаление всех данных из базы данных внесенных по этому '
                                        f'пользователю. Если требуется отключить рассылку пользователю и/или '
                                        f'изменить доступ пользователя к боту, рекомендуется изменить статус '
                                        f'пользователя или его телеграмма через кнопку "Редактировать" в предыдущем '
                                        f'меню.</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev32)


@dp.callback_query_handler(technik_menu_21.filter(level_t21='edit_user_data'))
async def del_users_data(call: CallbackQuery):
    """
    Тех меню. L33
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'<b>Пользователь</b> - для того, чтобы отредактировать фамилию пользователя\n'
                                        f'<b>ID Телеграмма</b> - для того, чтобы отредактировать номер телеграмма\n'
                                        f'<b>Статус</b> - для выбора пользователя или статуса отправки сообщений.',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev33)


@dp.callback_query_handler(technik_menu_22.filter(level_t22='delete_data'))
async def delete_data(call: CallbackQuery):
    """
    Тех меню. L35
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Выберите какой тип данных нужно удалить.',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev35)


@dp.callback_query_handler(technik_menu_33.filter(level_t33='edit_status'))
async def ed_status(call: CallbackQuery):
    """
    Тех меню. L41
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    user_name = call.from_user.first_name
    await dp.bot.edit_message_text(text=f'Изменение статуса пользователя позволит расширить или ограничить доступ '
                                        f'пользователя к данным в боте. Изменение статуса рассылки подключает '
                                        f'пользователя к рассылкие статистики отдела. Если у пользователя не включен '
                                        f'статус "подтверждена", то бот не сможет отправлять сообщения пользователю.\n '
                                        f'<i>Обратите внимание, что рассылка пользователю возможна только в том '
                                        f'случае, если пользователь отправил боту сообщение первым. Иначе попытка '
                                        f'отправки сообщения может вызвать ошибку программы, вплоть до ее '
                                        f'отключения.</i>',
                                   chat_id=user_id, message_id=current_msg, parse_mode=ParseMode.HTML,
                                   reply_markup=kb_tech_lev41)
