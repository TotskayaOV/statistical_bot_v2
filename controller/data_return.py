from .creating_dashbord import save_one_image
from .conversion_human_form import conversion_standard_timestamp
from .generating_output_data import create_one_day, personalized_data_period
from .creating_graphs import created_bar_name, horizontal_bar, created_bar
from loader import user_db
from config import name_tables, position_graps, name_string, name_us_string
from datetime import datetime, timedelta


def return_result_users_one_day(date_obj: str, user_id: str, new_pict=False):
    counting_for_marge_file = []
    general_string = ''
    users_string = '<b>Твои результаты:</b>\n'
    # counting_for_marge_file.append(general_pie_graf(date_obj))
    method_dict ={'general_portal': created_bar_name, 'j_counts': created_bar_name,
                  'j_times': created_bar_name, 'j_sla': horizontal_bar, 'calls': created_bar_name}
    for elem in name_tables:
        users_name = user_db.get_the('users', id=user_db.get_the('contacts_users', tg_id=user_id)[0])[1]
        result_tuple = create_one_day(table_name=elem, date_obj=date_obj, user_target=users_name)
        if result_tuple:
            if new_pict:
                counting_for_marge_file.append(method_dict.get(elem)(df=result_tuple[1], t_label=name_tables.get(elem),
                                                                file_name=f'{elem}-{user_id}',
                                                                right_position=position_graps.get(elem)))
            match elem:
                case 'j_times':
                    cnt_values = conversion_standard_timestamp(result_tuple[0])
                    user_values = conversion_standard_timestamp(result_tuple[2][0].get('values'))
                case 'j_sla':
                    cnt_values = f'{round(result_tuple[0], 1)}%'
                    user_values = f'{round(result_tuple[2][0].get("values"), 1)}%'
                case _:
                    cnt_values = str(result_tuple[0])
                    user_values = str(result_tuple[2][0].get("values"))
            general_string = general_string + name_string.get(elem) + ': ' + cnt_values + '\n'
            users_string = users_string  + name_us_string.get(elem) + ' - ' + user_values + '\n'
        else: counting_for_marge_file.append(0)
    # counting_for_marge_file.insert(4, 0)
    if new_pict:
        save_one_image(counting_for_marge_file, user_id)
    return (general_string + users_string)
    # counting_for_marge_file.append(horizontal_bar(date_obj))
    # counting_for_marge_file.append(general_pie_graf(date_obj))
    # done_image = save_one_image(counting_for_marge_file, date_obj)

def return_result_users_period(date_obj: str, user_id: str, new_pict=False):
    date_obj_on = datetime.strptime(date_obj, '%Y-%m-%d')
    date_in = str((date_obj_on - timedelta(days=7)).date())
    counting_for_marge_file = []
    general_string = '<b>Результаты отдела:</b>\n'
    users_string = '\n<b>Твои результаты:</b>\n'
    # counting_for_marge_file.append(general_pie_graf(date_obj))
    method_dict ={'general_portal': created_bar, 'j_counts': created_bar,
                  'j_times': created_bar, 'j_sla': created_bar, 'calls': created_bar}
    for elem in name_tables:
        users_name = user_db.get_the('users', id=user_db.get_the('contacts_users', tg_id=user_id)[0])[1]
        result_tuple = personalized_data_period(table_name=elem, date_dict={'date_in': date_in, 'date_on': date_obj},
                                                name_user=users_name)
        if result_tuple:
            general_string = general_string + '<u>' +  name_string.get(elem) + '</u>\n'
            users_string = users_string + '<u>' + name_us_string.get(elem) + '</u>\n'
            if new_pict:
                counting_for_marge_file.append(method_dict.get(elem)(df=result_tuple[0], t_label=name_tables.get(elem),
                                                                file_name=f'{elem}-{user_id}',
                                                                right_position=position_graps.get(elem)))
            for days_elem in result_tuple[1]:
                match elem:
                    case 'j_times':
                        cnt_values = conversion_standard_timestamp(days_elem.get('total'))
                        user_values = conversion_standard_timestamp(days_elem.get('values'))
                    case 'j_sla':
                        cnt_values = f"{round(days_elem.get('total'), 1)}%"
                        user_values = f"{round(days_elem.get('values'), 1)}%"
                    case _:
                        cnt_values = str(days_elem.get('total'))
                        user_values = str(days_elem.get('values'))
                general_string = general_string + days_elem.get('date') + ': ' + cnt_values + '\n'
                users_string = users_string  + days_elem.get('date') + ': ' + user_values + '\n'
        else: counting_for_marge_file.append(0)
    # counting_for_marge_file.insert(4, 0)
    if new_pict:
        save_one_image(counting_for_marge_file, user_id)
    return (general_string + users_string)
