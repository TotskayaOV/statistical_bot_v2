from loader import dp
from aiogram.types import Message, InputFile, ContentTypes, ParseMode
from aiogram.dispatcher import FSMContext
from view.keyboards.standart import kb_yesterday
from view.keyboards.inline import kb_daily_report
from controller import return_result_users_one_day, deleting_temporary_files, check_one_day_report
from view.states import UserStats


@dp.message_handler(commands=['result'], state=None)
async def start_user_request(message: Message, admin: bool, coordinator: bool):
    if admin or coordinator:
        await message.answer(text='Напишите дату в формате ГГГГ-ММ-ДД или нажмите кнопку 👇🏻', reply_markup=kb_yesterday)
        await UserStats.next()
    else:
        await message.answer('У вас нет доступа к этой функции')

@dp.message_handler(state=UserStats.user_date, content_types=ContentTypes.ANY)
async def date_catch(message: Message, state: FSMContext):
    try:
        date_obj = message.text
        user_id = message.from_user.id
        photo = check_one_day_report(date_obj, user_id)
        if photo:
            text = return_result_users_one_day(date_obj, user_id)
            checking_file_deletion = False
        else:
            text = return_result_users_one_day(date_obj, user_id, new_pict=True)
            photo = InputFile(f"./cred/merged_images-{user_id}.png")
            checking_file_deletion = True
        await dp.bot.send_photo(chat_id=message.chat.id, photo=photo, caption=text,
                                reply_markup=kb_daily_report(date_obj), parse_mode=ParseMode.HTML)
    except ValueError:
        await message.answer(text='Ошибка ввода даты.\nНапишите дату в формате 2023-01-01',
                             reply_markup=kb_yesterday)
        await UserStats.user_date.set()
    except Exception as err:
        await message.answer(text=f'Возникла непредвиденная ошибка\n{err}',
                             reply_markup=kb_yesterday)
        await state.reset_data()
        await state.finish()
    else:
        await state.reset_data()
        await state.finish()
        if checking_file_deletion:
            deleting_temporary_files(user_id)
