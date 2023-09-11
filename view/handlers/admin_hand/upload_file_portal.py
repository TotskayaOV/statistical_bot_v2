import os
from aiogram.dispatcher import FSMContext
from aiogram.types import Message, ContentTypes, CallbackQuery, ParseMode
from datetime import datetime, timedelta

from loader import dp
from view.keyboards.inline import kb_date, kb_cancel_fsm
from view.keyboards.standart import kb_cancel
from view.states import UploadFilePortals
from view.callback import admin_menu_31, menu_2_date


@dp.callback_query_handler(admin_menu_31.filter(level_a31='portal_file'))
async def upload_calls_count(call: CallbackQuery, admin: bool):
    """
    Переход в state загрузки файла проверенных анкет на портале
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    if admin:
        await dp.bot.edit_message_text(text=f'Введите дату в формате <b>ГГГГ-ММ-ДД</b> или выберите из предложенных👇🏻:',
                                       chat_id=user_id, message_id=current_msg, reply_markup=kb_date(),
                                       parse_mode=ParseMode.HTML)
        await UploadFilePortals.catch_date.set()
    else:
        dp.bot.edit_message_text(text=f'У вас нет доступа к этой функции',
                                 chat_id=user_id, message_id=current_msg)


@dp.callback_query_handler(menu_2_date.filter(date_priority='yesterday'), state=UploadFilePortals.catch_date)
async def file_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Запрос загрузки файла за вчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=1)
    await state.update_data({'catch_date': str(date_yesterday)})
    await dp.bot.edit_message_text(text=f'Загрузите файл проверок портала за {date_yesterday}:',
                                    chat_id=user_id, message_id=current_msg, reply_markup=kb_cancel_fsm,
                                       parse_mode=ParseMode.HTML)
    await UploadFilePortals.catch_file.set()


@dp.callback_query_handler(menu_2_date.filter(date_priority='bf_yesterday'), state=UploadFilePortals.catch_date)
async def file_bf_yesterday_date_catch(call: CallbackQuery, state: FSMContext):
    """
    Запрос загрузки файла за позавчера от текущей даты
    """
    current_msg = call.message.message_id
    user_id = call.from_user.id
    date_yesterday = datetime.now().date() - timedelta(days=2)
    await state.update_data({'catch_date': str(date_yesterday)})
    await dp.bot.edit_message_text(text=f'Загрузите файл проверок портала за {date_yesterday}:',
                                    chat_id=user_id, message_id=current_msg, reply_markup=kb_cancel_fsm,
                                       parse_mode=ParseMode.HTML)
    await UploadFilePortals.catch_file.set()


@dp.message_handler(state=UploadFilePortals.catch_date, content_types=ContentTypes.ANY)
async def file_date_catch(message: Message, state: FSMContext):
    """
    Проверка ввода даты и запрос загрузки файла
    """
    try:
        data_obj = message.text
        up_data = datetime.strptime(data_obj, '%Y-%m-%d')
    except:
        await message.answer(text='Ошибка ввода даты. Введите дату в формате <b>ГГГГ-ММ-ДД</b>',
                             parse_mode=ParseMode.HTML)
        UploadFilePortals.catch_date.set()
    else:
        await state.update_data({'catch_date': data_obj})
        await message.answer(text=f'Загрузите файл проверок портала за {data_obj}:', reply_markup=kb_cancel)
        await UploadFilePortals.catch_file.set()


@dp.message_handler(state=UploadFilePortals.catch_file, content_types=ContentTypes.ANY)
async def portals_catch(message: Message, state: FSMContext):
    await message.answer(text=f'Кнопка в разработке')
    await state.reset_data()
    await state.finish()
    # if document := message.document:
    #     await state.update_data({'catch_file': True})
    #     await document.download(destination_file=f'./cred/{document.file_name}')
    #     try:
    #         os.rename(f'./cred/{document.file_name}', './cred/call.csv')
    #     except:
    #         os.remove('./cred/call.csv')
    #         os.rename(f'./cred/{document.file_name}', './cred/call.csv')
    #     finally:
    #         data = await state.get_data()
    #         try:
    #             result_upload = recording_call_database()
    #         except Exception as err:
    #             await message.answer(text=f'Ошибка загрузки данных. Проверьте файл: расширение, кодировку, формат '
    #                                       f'данных.\nИли передайте данные об ошибке: {err}')
    #             await state.reset_data()
    #             await state.finish()
    #         else:
    #             await state.reset_data()
    #             await state.finish()
    #             if result_upload:
    #                 await message.answer(text='Данные количества выполненых звонков загружены',
    #                                      reply_markup=kb_admin_lev21)
    #             else:
    #                 await message.answer(text='Ошибка загрузки данных количества выполненных звонков. '
    #                                           'Проверьте файл:'
    #                                           'расширение, кодировку, формат данных.', reply_markup=kb_admin_lev21)
    #         finally:
    #             try:
    #                 os.remove('./cred/call.csv')
    #             except Exception as err:
    #                 await message.answer(text=f'Ошибка удаления файла: {err}')
    #                 await state.reset_data()
    #                 await state.finish()
