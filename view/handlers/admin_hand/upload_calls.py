import os
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode

from loader import dp
from view.keyboards.inline import kb_admin_lev21, kb_cancel_fsm
from view.states import UploadFileCalls
from view.callback import admin_menu_21
from controller import recording_call_database



@dp.callback_query_handler(admin_menu_21.filter(level_a21='calls'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state загрузки файла выполненных заявок в  Jira
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Загрузите файл данных с <b>количеством выполненных звонков</b>',
                                    chat_id=user_id, message_id=current_msg, reply_markup=kb_cancel_fsm,
                                       parse_mode=ParseMode.HTML)
        await UploadFileCalls.next()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)

@dp.message_handler(state=UploadFileCalls.catch_file, content_types=ContentTypes.ANY)
async def calls_catch(message: Message, state: FSMContext):
    if document := message.document:
        await state.update_data({'catch_file': True})
        await document.download(destination_file=f'./cred/{document.file_name}')
        try:
            os.rename(f'./cred/{document.file_name}', './cred/call.csv')
        except:
            os.remove('./cred/call.csv')
            os.rename(f'./cred/{document.file_name}', './cred/call.csv')
        finally:
            data = await state.get_data()
            try:
                result_upload = recording_call_database()
            except Exception as err:
                await message.answer(text=f'Ошибка загрузки данных. Проверьте файл: расширение, кодировку, формат '
                                          f'данных.\nИли передайте данные об ошибке: {err}')
                await state.reset_data()
                await state.finish()
            else:
                await state.reset_data()
                await state.finish()
                if result_upload:
                    await message.answer(text='Данные количества выполненых звонков загружены',
                                         reply_markup=kb_admin_lev21)
                else:
                    await message.answer(text='Ошибка загрузки данных количества выполненных звонков. '
                                              'Проверьте файл:'
                                              'расширение, кодировку, формат данных.', reply_markup=kb_admin_lev21)
            finally:
                try:
                    os.remove('./cred/call.csv')
                except Exception as err:
                    await message.answer(text=f'Ошибка удаления файла: {err}')
                    await state.reset_data()
                    await state.finish()
