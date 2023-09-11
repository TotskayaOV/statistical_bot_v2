import os
import sqlite3

from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

from modul import DataBase, User, Call, Technical, Jira, Portal, Picture
# from config import db_path
# from sending_messages import notify


memory = MemoryStorage()

bot = Bot(os.getenv('TOKEN'))
dp = Dispatcher(bot, storage=memory)
db = DataBase()

user_db = User()
call_db = Call()
jira_db = Jira()
technical_db = Technical()
portal_db = Portal()
report_db = Picture()
# # log_id = os.getenv('LOG_ID')
# admin_id = os.getenv('ADMIN_ID')



async def on_startup(_):
    print('Bot started!')
    try:
        user_db.create_table_users()
        user_db.create_table_users_contacts()
        call_db.create_table_calls()
        jira_db.create_table_jira_sla()
        jira_db.create_table_jira_time()
        jira_db.create_table_jira_count()
        technical_db.create_table_number_row()
        technical_db.create_table_datetime()
        technical_db.create_table_delimiters()
        portal_db.create_table_portal()
        portal_db.create_general_data()
        report_db.create_table_reports()
        print('DataBase .... Ok!')
    except sqlite3.OperationalError:
        print('DataBase .... фиг вам, а не датабаза')


async def on_shutdown(_):
    user_db.disconnect()
    call_db.disconnect()
    jira_db.disconnect()
    technical_db.disconnect()
    portal_db.disconnect()
    report_db.disconnect()