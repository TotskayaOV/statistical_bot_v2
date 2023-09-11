from aiogram.types import CallbackQuery, InputMediaPhoto, InputFile, ParseMode

from loader import dp
from view.keyboards.inline import kb_daily_report
from view.callback import date_return
from controller import return_result_users_one_day, check_record_img, \
    return_result_users_period, check_one_period_report, check_record_period_img, check_one_day_report, \
    deleting_temporary_files
from loader import bot

@dp.callback_query_handler(date_return.filter(button='one_day'))
async def one_day_report_users(call: CallbackQuery):
    try:
        current_msg = call.message.message_id
        date_obj = call.data.split(':')[-1]
        user_id = call.from_user.id
        PhotoSize = call.message.photo[-1]
        file_info = PhotoSize.file_id
        check_record_period_img(date_obj, user_id, file_info)
        photo = check_one_day_report(date_obj, user_id)
        if photo:
            text = return_result_users_one_day(date_obj, user_id)
        else:
            text = return_result_users_one_day(date_obj, user_id, new_pict=True)
            photo = InputFile(f"./cred/merged_images-{user_id}.png")
        await bot.edit_message_media(media=InputMediaPhoto(media=photo, caption=text, parse_mode=ParseMode.HTML),
                                     chat_id=user_id, message_id=current_msg, reply_markup=kb_daily_report(date_obj))
    except Exception as err:
        text = f'Возникла непредвиденная ошибка\n{err}'
        await bot.edit_message_caption(chat_id=user_id, message_id=current_msg, caption=text,
                                       reply_markup=kb_daily_report(date_obj, step=False))
    else:
        deleting_temporary_files(user_id)


@dp.callback_query_handler(date_return.filter(button='period'))
async def period_report_users(call: CallbackQuery):
    try:
        current_msg = call.message.message_id
        date_obj = call.data.split(':')[-1]
        user_id = call.from_user.id
        PhotoSize = call.message.photo[-1]
        file_info = PhotoSize.file_id
        check_record_img(date_obj, user_id, file_info)
        photo = check_one_period_report(date_obj, user_id)
        if photo:
            text = return_result_users_period(date_obj, user_id)
        else:
            text = return_result_users_period(date_obj,user_id,new_pict=True)
            photo = InputFile(f"./cred/merged_images-{user_id}.png")
        await bot.edit_message_media(media=InputMediaPhoto(
                media=photo, caption=text, parse_mode=ParseMode.HTML),
                chat_id=user_id, message_id=current_msg,
                reply_markup=kb_daily_report(date_obj, step=False))
    except Exception as err:
        text = f'Возникла непредвиденная ошибка\n{err}'
        await bot.edit_message_caption(chat_id=user_id, message_id=current_msg, caption=text,
                                   reply_markup=kb_daily_report(date_obj, step=False))
    else:
         deleting_temporary_files(user_id)
