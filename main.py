from aiogram import executor
from view import dp
from loader import on_startup, on_shutdown
import middleware


async def on_start(_):
    print('Start Bot')


if __name__ == '__main__':
    middleware.setup(dp)
    executor.start_polling(dispatcher=dp,
                           skip_updates=True,
                           on_startup=on_startup,
                           on_shutdown=on_shutdown)




# user_db = User()
# jira_db = Jira()
# jira_db.create_table_jira_count()
# jira_db.add_jira_count({'date_jira': '2023-06-15', 'user_id': 1, 'count_task': 10})
# # jira_db.remove_jira('j_counts', user_id=1)
# jira_db.update_jira(name_table='j_counts', name_col='count_task', new_data={'value': 12, 'id': 6})
# print(result)


# print(parsing_call_data(read_csv_file('./cred/call.csv', 'UTF-8', 2, ';')))
# print(checking_date_string('16.06.2023', '%d.%m.%Y'))