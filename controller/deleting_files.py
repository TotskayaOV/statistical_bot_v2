import os

from loader import jira_db, portal_db, call_db

def deleting_temporary_files(user_id):
    if os.path.isfile(f"./cred/merged_images-{user_id}.png"):
        os.remove(f"./cred/merged_images-{user_id}.png")
    if os.path.isfile(f'./cred/calls-{user_id}.jpg'):
        os.remove(f'./cred/calls-{user_id}.jpg')
    if os.path.isfile(f'./cred/j_counts-{user_id}.jpg'):
        os.remove(f'./cred/j_counts-{user_id}.jpg')
    if os.path.isfile(f'./cred/general-{user_id}.jpg'):
        os.remove(f'./cred/general-{user_id}.jpg')
    if os.path.isfile(f'./cred/portal-{user_id}.jpg'):
        os.remove(f'./cred/portal-{user_id}.jpg')
    if os.path.isfile(f'./cred/j_sla-{user_id}.jpg'):
        os.remove(f'./cred/j_sla-{user_id}.jpg')
    if os.path.isfile(f'./cred/j_times-{user_id}.jpg'):
        os.remove(f'./cred/j_times-{user_id}.jpg')


def deleted_data_for_date(obj_data: str, date_data: str):
    """
    Удаление данных из БД
    """
    print(date_data, obj_data)
    match obj_data:
        case 'j_sla': jira_db.remove_jira('j_sla', date_wd=date_data)
        case 'j_time': jira_db.remove_jira('j_times', date_wd=date_data)
        case 'j_count': jira_db.remove_jira('j_count', date_wd=date_data)
        case 'portal': portal_db.remove_portal('general_portal', date_wd=date_data)
        case 'general': portal_db.remove_portal('general_data', date_wd=date_data)
        case 'call': call_db.remove_call('calls', date_wd=date_data)
