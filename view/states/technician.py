from aiogram.dispatcher.filters.state import StatesGroup, State

class NewUser(StatesGroup):
    user_name = State()
    user_status = State()

class NewTgID(StatesGroup):
    user_id = State()
    tg_id = State()

class EditUser(StatesGroup):
    user_id = State()
    user_name = State()

class EditTgId(StatesGroup):
    user_id = State()
    tg_id = State()

class EditUserStatus(StatesGroup):
    user_id = State()
    user_status = State()

class EditMail(StatesGroup):
    user_id = State()
    mail_status = State()

class DownlFile(StatesGroup):
    user_pass = State()

class DelUser(StatesGroup):
    user_id = State()

class DelContacts(StatesGroup):
    user_id = State()

class DelJiraSLA(StatesGroup):
    date_data = State()

class DelJiraTime(StatesGroup):
    date_data = State()

class DelJiraCount(StatesGroup):
    date_data = State()

class DelPortal(StatesGroup):
    date_data = State()

class DelGeneralData(StatesGroup):
    date_data = State()

class DelCalls(StatesGroup):
    date_data = State()

class NewDelimiters(StatesGroup):
    name_file = State()
    new_value = State()

class NewDetetime(StatesGroup):
    name_file = State()
    new_value = State()

class NewNumStr(StatesGroup):
    name_file = State()
    new_value = State()

class PictCatch(StatesGroup):
    user_pict = State()
