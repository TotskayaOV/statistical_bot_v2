import os
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes, CallbackQuery

from loader import dp
from view.keyboards.inline import kb_admin_lev32, kb_cancel_fsm
from view.states import UploadFileTime
from view.callback import admin_menu_32
from controller import recording_jira_database



@dp.callback_query_handler(admin_menu_32.filter(level_a32='jira_time'))
async def upload_jira_time(call: CallbackQuery, admin: bool):
    """
    Переход в state загрузки файла времени проверки Jira
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Загрузите файл данных времени выполнения заявок Jira',
                                    chat_id=user_id, message_id=current_msg, reply_markup=kb_cancel_fsm)
        await UploadFileTime.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)

@dp.message_handler(state=UploadFileTime.catch_file, content_types=ContentTypes.ANY)
async def jira_time_catch(message: Message, state: FSMContext):
    if document := message.document:
        await state.update_data({'catch_file': True})
        await document.download(destination_file=f'./cred/{document.file_name}')
        try:
            os.rename(f'./cred/{document.file_name}', './cred/time.csv')
        except:
            os.remove('./cred/time.csv')
            os.rename(f'./cred/{document.file_name}', './cred/time.csv')
        finally:
            data = await state.get_data()
            try:
                result_upload = recording_jira_database('time')
            except Exception as err:
                await message.answer(text=f'Ошибка загрузки данных. Проверьте файл: расширение, кодировку, формат '
                                          f'данных.\nИли передайте данные об ошибке: {err}')
                await state.reset_data()
                await state.finish()
            else:
                await state.reset_data()
                await state.finish()
                if result_upload:
                    await message.answer(text='Данные времени выполнения заявок Jira загружены',
                                         reply_markup=kb_admin_lev32)
                else:
                    await message.answer(text='Ошибка загрузки данных времени выполнения заявок Jira. Проверьте файл:'
                                              'расширение, кодировку, формат данных.', reply_markup=kb_admin_lev32)
            finally:
                try:
                    os.remove('./cred/time.csv')
                except Exception as err:
                    await message.answer(text=f'Ошибка удаления файлов: {err}')
                    await state.reset_data()
                    await state.finish()
