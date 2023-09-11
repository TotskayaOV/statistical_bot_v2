import os
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode, InputFile
from datetime import datetime, timedelta

from loader import dp, technical_db
from view.keyboards.inline import kb_tech_lev22, kb_cancel_fsm
from view.states import DownlFile
from view.callback import technik_menu_22


@dp.callback_query_handler(technik_menu_22.filter(level_t22='download_data'))
async def download_data(call: CallbackQuery, admin: bool):
    """
    Тех меню. L34
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите пароль для доступа к функции скачивания:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_cancel_fsm,
                                       parse_mode=ParseMode.HTML)
        await DownlFile.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.message_handler(state=DownlFile.user_pass, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка пароля и отправка файла
    """
    user_pass = message.text
    if user_pass == technical_db.get_delimiters(files_name='pass')[0]:
        path = './cred/dp_bot_db.db'
        await message.answer_document(InputFile(path))
        await message.answer(text=f'При ошибочной загрузке данных, есть возможность удалить загруженные данные. '
                                  f'Для того, чтобы скачать данные из базы данных потребуется ввод пароля.',
                             reply_markup=kb_tech_lev22)
        await state.reset_data()
        await state.finish()
    else:
        await message.answer(text='Ошибка ввода пароля. Введите пароль еще раз или нажмите "Отмена"',
                             reply_markup=kb_cancel_fsm)
        await DownlFile.user_pass.set()
