from loader import report_db
from datetime import datetime, timedelta

def check_one_day_report(date_obj: str, tg_id: int):
    id_pick = date_obj.replace('-', '') + str(tg_id)
    result_check = report_db.get_reports(id_repo=id_pick)
    if result_check:
        return result_check[2]


def check_one_period_report(date_obj: str, tg_id: int):
    date_obj_on = datetime.strptime(date_obj, '%Y-%m-%d')
    date_in = str((date_obj_on - timedelta(days=7)).date())
    id_pick = date_obj.replace('-', '') + date_in.replace('-', '') + str(tg_id)
    result_check = report_db.get_reports(id_repo=id_pick)
    if result_check:
        return result_check[2]



def check_record_img(date_obj: str, tg_id: int, pick_id: str):
    if check_one_day_report(date_obj, tg_id) == None:
        report_db.add_reports({'id_repo': date_obj.replace('-', '') + str(tg_id),
                               'url_str': pick_id})

def check_record_period_img(date_obj: str, tg_id: int, pick_id: str):
    if check_one_period_report(date_obj, tg_id) == None:
        date_obj_on = datetime.strptime(date_obj, '%Y-%m-%d')
        date_in = str((date_obj_on - timedelta(days=7)).date())
        id_pick = date_obj.replace('-', '') + date_in.replace('-', '') + str(tg_id)
        report_db.add_reports({'id_repo': id_pick, 'url_str': pick_id})
