import polars as pl

from datetime import datetime

from loader import technical_db, user_db, portal_db, jira_db, call_db

from modul import read_csv_file

from modul import parsing_call_data, parsing_jira_data, parsing_portal_data

def checking_date_string(null_date: str, intended_format: str, start_point=0):
    """
    Функция проверяет возможность перевода строкового формата даты в объект datetime. Если предполагаемый формат
    не подходит, то двигается вниз по списку с другими возможным вариантам
    :param null_date: дата
    :param intended_format:
    :return:
    """
    suggested_formats = ['%Y.%m.%d', '%d.%m.%Y', '%Y-%m-%d', '%d-%m-%Y', '%Y:%m:%d', '%d:%m:%Y',
                         '%d.%b.%y', '%y.%b.%d', '%b %d %Y', '%d %b %Y', '%Y %d %b', '%Y %b %d',
                         '%d-%m-%Y', '%Y-%m-%d']
    try:
        dt = datetime.strptime(null_date, intended_format).date()
        return dt
    except ValueError:
        if start_point < len(suggested_formats):
            return checking_date_string(null_date, suggested_formats[start_point], start_point=start_point+1)
        else:
            return 0


def writing_db_check_availability(tuple_data: list, date_obj: datetime, get_dict: dict, record_method: classmethod,
                                  update_method: classmethod, name_table: str, name_col: str):
    """
    Проверяет наличие записи за дату в словаре из БД. Если запись есть производит перезапись, если нет - добавление
    :param tuple_data: лист кортежей (количество, user_id)
    :param date_obj: дата
    :param get_dict: словарь с записями из БД {id_записи: user_id}
    :param record_method: метод для записи в БД
    :param update_method: метод для обновления в БД
    :param name_table: название таблицы в БД
    :param name_col: название столбца для значения
    """
    for elem in tuple_data:
        if get_dict.get(elem[1], False) is False:
            record_method({'date_wd': date_obj, 'user_id': elem[1], 'value': elem[0]})
        else:
            update_method(name_table, name_col, {'value': elem[0], 'id': get_dict.get(elem[1])})


def recording_call_database():
    """
    Функция получает список с данными, произведя чтение данных из файла. Формирует фрейм данных добавляя вторым
    столбцом 1. Группирует фрейм по имени применяя агрегирующую функцию sum(). Объединяет с фреймом данных
    полученным из таблицы users базы данных. После удаления столбца со строковыми данными (фамилия) передает
    данные в функцию для записи в базу данных.
    :return: boolean
    """
    tuple_data = parsing_call_data(read_csv_file('./cred/call.csv', 'UTF-8',
                                                 2, technical_db.get_delimiters(files_name='call')[0]))
    datetime_obj = checking_date_string(tuple_data[0], technical_db.get_datetime(files_name='call')[0])
    if not datetime_obj:
        return False
    else:
        df = pl.DataFrame({'name': tuple_data[1], 'call': 1})
        df = df.groupby('name').agg(pl.col('call').sum())
        users_data = user_db.get_users()
        df_names = pl.DataFrame({'index': [elem[0] for elem in users_data], 'name': [elem[1] for elem in users_data]})
        df = df.join(df_names, on='name', how='inner')
        df = df.drop('name')
        get_tuples = call_db.get_call('calls', date_wd=datetime_obj)
        if get_tuples: get_dict = {elem[2]: elem[0] for elem in get_tuples}
        else: get_dict = {0: 0}
        writing_db_check_availability(df.rows(), datetime_obj, get_dict,
                                      record_method=call_db.add_call, update_method=call_db.update_call,
                                      name_table='calls', name_col='count_call')
        return True


def recording_jira_database(type_jira_data: str):
    """
    Функция получает словарь с данными, произведя чтение данных из файла, подставляя аргумент в указанный путь.
    В цикле по словарю формирует фреймы данных, объединяя их поочердно с фреймом данных полученным из таблицы
    users базы данных. Производит группировку по столбцу 'names', применяя агрегирующую функцию в зависимости
    от аргумента. После удаления столбца со строковыми данными (фамилия) передает данные в функцию для записи
    в базу данных, беря заданные значения названий таблиц, строк и методов из заданного вначале функции
    словаря processing_dictionary по ключу аргументу.
    :param type_jira_data: маркер типа загружаемых данных из Jira (count, time, sla)
    :return: boolean
    """
    data = parsing_jira_data(read_csv_file(f'./cred/{type_jira_data}.csv', 'UTF-8',
                                           technical_db.get_numbers_start_row(files_name=type_jira_data)[0],
                                           technical_db.get_delimiters(files_name=type_jira_data)[0]),
                             technical_db.get_numbers_start_row(files_name=f'in_{type_jira_data}')[0])
    processing_dictionary = {
        'time': {"record_method": jira_db.add_jira_time, "name_table": 'j_times', "name_col": 'time_task'},
        'count': {"record_method": jira_db.add_jira_count, "name_table": 'j_counts', "name_col": 'count_task'},
        "sla": {"record_method": jira_db.add_jira_sla, "name_table": 'j_sla', "name_col": 'sla_task'}}
    users_data = user_db.get_users()
    df_names = pl.DataFrame({'index': [elem[0] for elem in users_data], 'name': [elem[1] for elem in users_data]})
    for date_obj, list_data in data.items():
        datetime_obj = checking_date_string(date_obj, technical_db.get_datetime(files_name=type_jira_data)[0])
        if not datetime_obj: return False
        else:
            df = pl.DataFrame({'name': [elem[0] for elem in list_data if elem[1]!= ''],
                                'value': [float(elem[1]) for elem in list_data if elem[1]!= '']})
            if type_jira_data == 'count': df = df.groupby('name').agg(pl.col('value').sum())
            else: df = df.groupby('name').agg(pl.col('value').mean())
            df = df.join(df_names, on='name', how='inner')
            df = df.drop('name')
            get_tuples = jira_db.get_jira(processing_dictionary.get(type_jira_data).get("name_table"),
                                          date_wd=datetime_obj)
            if get_tuples: get_dict = {elem[2]: elem[0] for elem in get_tuples}
            else: get_dict = {0: 0}
            writing_db_check_availability(df.rows(), datetime_obj, get_dict,
                                          record_method=processing_dictionary.get(type_jira_data).get("record_method"),
                                          update_method=jira_db.update_jira,
                                          name_table=processing_dictionary.get(type_jira_data).get("name_table"),
                                          name_col=processing_dictionary.get(type_jira_data).get("name_col"))
    return True


def recording_portal_database(type_portal_data, date_obj):
    """
    Функция получает список кортежей с данными, произведя чтение данных из файла, подставляя аргумент в указанный
    путь. Формирует фрейм данных. Объединяет с фреймом данных полученным из таблицы users базы данных.
    Производит группировку по столбцу 'names'. После удаления столбца со строковыми данными (фамилия) передает данные
    в функцию для записи в базу данных.
    :param type_portal_data: название файла, таблицы в базе данных, значения в технических талицах
    :param date_obj: строковое значение даты
    :return: boolean
    """
    data = parsing_portal_data(read_csv_file(f'./cred/{type_portal_data}.csv', 'UTF-8',
                                             technical_db.get_numbers_start_row(files_name=type_portal_data)[0],
                                             technical_db.get_delimiters(files_name=type_portal_data)[0]))
    datetime_obj = checking_date_string(date_obj, technical_db.get_datetime(files_name=type_portal_data)[0])
    if not datetime_obj:
        return False
    else:
        users_data = user_db.get_users()
        df_names = pl.DataFrame({'index': [elem[0] for elem in users_data], 'name': [elem[1] for elem in users_data]})
        df = pl.DataFrame({'name': [elem[0] for elem in data], 'value': [elem[1] for elem in data]})
        df = df.join(df_names, on='name', how='inner')
        df = df.drop('name')
        get_tuples = portal_db.get_portal (type_portal_data, date_wd=datetime_obj)
        if get_tuples: get_dict = {elem[2]: elem[0] for elem in get_tuples}
        else: get_dict = {0: 0}
        writing_db_check_availability(df.rows(), datetime_obj, get_dict,
                                      record_method=portal_db.add_portal, update_method=portal_db.update_portal,
                                      name_table=type_portal_data, name_col='count_verify')
        return True


def added_users_from_db(users_data: dict) -> bool:
    """
    Запись нового пользователя в базу данных
    """
    try:
        user_db.add_user({'name': users_data.get('user_name'), 'status': users_data.get('user_status')})
        return True
    except:
        return False

def added_tg_id_from_db(users_data: dict) -> bool:
    """
    Запись нового tg_id в базу данных
    """
    try:
        user_db.add_contacts({'fk_users': users_data.get('user_id'), 'tg_id': users_data.get('tg_id'),
                              'status_mail': 0})
        return True
    except:
        return False


def update_user_data_from_db(edit_object: str, user_data: dict) -> bool:
    """
    Обновление данных пользователей в базе данных
    """
    match edit_object:
        case 'user name': print(user_db.update_user_name({'id': user_data.get('user_id'),
                                                    'name': user_data.get('user_name')}))
        case 'user status': user_db.update_user_status({'id': user_data.get('user_id'),
                                                        'status': user_data.get('user_status')})
        case 'tg id': user_db.update_tg_id({'id': user_data.get('user_id'), 'tg id': user_data.get('tg_id')})
        case 'mail status': user_db.update_mail_status({'id': user_data.get('user_id'),
                                                        'status': user_data.get('mail_status')})

