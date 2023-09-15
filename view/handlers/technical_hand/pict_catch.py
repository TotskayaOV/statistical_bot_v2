from loader import dp
from aiogram.types import Message, ContentTypes
from aiogram.dispatcher import FSMContext
from controller import record_pict_id_for_null
from view.states import PictCatch


@dp.message_handler(commands=['pict_catch'], state=None)
async def mes_start(message: Message, admin: bool):
    """
    загрузка статических фото в базу данных. используется только при первом включении
    """
    if admin:
        await message.answer(f'Привет, грузи свое фото')
        await PictCatch.next()
@dp.message_handler(state=PictCatch.user_pict, content_types=ContentTypes.ANY)
async def date_catch(message: Message, state: FSMContext):
    PhotoSize = message.photo[-1]
    file_info = PhotoSize.file_id
    record_pict_id_for_null(1, file_info)
    await message.answer(f'Готово')
    await state.reset_data()
    await state.finish()
