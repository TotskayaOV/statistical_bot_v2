from loader import user_db, technical_db


def get_name_user_data_to_str() -> str:
    """
    Формирует строку со списком пользователей
    """
    users_list = user_db.get_users()
    result_string = 'Список пользователей\n\n<u>id</u>\t|\t<u>Фамилия</u>\t|\t<u>статус</u>\n'
    for users_tuple in users_list:
        result_string += f'{users_tuple[0]}. {users_tuple[1]}: {users_tuple[2]}\n'
    return result_string


def get_tg_user_data_to_str() -> str:
    """
    Формирует строку со id телеграмма и статусом рассылки
    """
    users_dict = {elem[0]: elem[1] for elem in user_db.get_users()}
    tg_list = user_db.get_contacts()
    result_string = 'Список пользователей\n\n<u>id</u>\t|\t<u>Фамилия</u>\t|\tID телеграма\t|\t<u>статус</u>\n'
    for tg_tuple in tg_list:
        match tg_tuple[2]:
            case 0: status = 'не активна'
            case 1: status = 'активна'
        result_string += f'{tg_tuple[0]}. {users_dict.get(tg_tuple[0])} - {tg_tuple[1]}: рассылка {status}\n'
    return result_string


def get_params_file(name_param: str) -> str:
    """
    Возвращает заданные на текущий момент параметры извлечения данных
    """
    match name_param:
        case 'delimiters':
            return ''.join([f'{elem[0]}: {elem[1]}\n' for elem in technical_db.get_all(name_param) if elem[0] != 'pass'])
        case 'date_str':
            return ''.join([f'{elem[0]}: {elem[1]}\n' for elem in technical_db.get_all(name_param)])
        case 'numbers_start_row':
            return ''.join([f'{elem[0]}: {elem[1]}\n' for elem in technical_db.get_all(name_param) if 'in' not in elem[0]])


def updating_data_for_parsing(name_table: str, name_file: str, new_value: str):
    """
    Изменение данных для парсинга файлов
    :param name_table: delimiters, datetime, num_row
    :param name_file: count, time, sla, general_portal, call
    """
    match name_table:
        case 'delimiters': technical_db.update_delimiters({'simbol_delimiter': new_value, 'files_name': name_file})
        case 'datetime': technical_db.update_datetime({'simbol_datetime': new_value, 'files_name': name_file})
        case 'num_row': technical_db.update_numbers_start_row({'num_row': new_value, 'files_name': name_file})
