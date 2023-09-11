from aiogram.types import Message, ReplyKeyboardRemove, CallbackQuery
from aiogram.dispatcher.filters import Text
from aiogram.dispatcher import FSMContext


from loader import dp
from view.callback import button_cancel


@dp.message_handler(Text(equals='Отмена'), state='*')
async def state_st_stop(message: Message, state: FSMContext):
    await state.reset_state()
    await state.finish()
    await message.answer(text='🆗 Выход из режима ввода данных.', reply_markup=ReplyKeyboardRemove())


@dp.callback_query_handler(button_cancel.filter(cansel_fsm='cancel_fsm'), state='*')
async def state_inl_stop(call: CallbackQuery, state: FSMContext):
    chat_id = call.from_user.id
    await state.reset_state()
    await state.finish()
    await dp.bot.send_message(chat_id, text='🆗 Выход из режима ввода данных.')
