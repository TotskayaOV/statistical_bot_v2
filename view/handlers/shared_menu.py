from loader import dp
from aiogram.types import Message
from view.keyboards.inline import kb_general_admin_menu, kb_general_user_menu


@dp.message_handler(commands=['menu'])
async def mes_start(message: Message, admin: bool, coordinator: bool):
    user_id = message.from_user.id
    user_name = message.from_user.first_name
    if admin:
        await message.answer(f'Привет, {user_name}!\nВыбери за кого будешь рулить 😎',
                             reply_markup=kb_general_admin_menu)
    elif coordinator:
        await message.answer(f'Привет, {user_name}! 🤓\n',
                             reply_markup=kb_general_user_menu)

