def parsing_call_data(data_list: list):
    """
    Возвращает список фамилий пользователей
    :param data_list: список строк
    :return: дата, список фамилий
    """
    names_list = [elem[2].split(" ")[0].replace('"', "") for elem in data_list]
    date_obj = data_list[0][0].split(' ')[0].replace('"', "")
    return (date_obj, names_list)


def parsing_jira_data(data_list: list, num_row: int):
    """
    Возвращает словарь с датой в качестве ключа и списком кортежей
    :param data_list: список списков строк
    :param num_row: с какой строки начинать читать данные в списке (для исключения Last 7 days)
    :return: {дата: (Фамилия, значение), }
    """
    names_list = data_list[0]
    result_dict = {}
    for index_data in range(num_row, len(data_list)):
        temp_list_date = []
        for index_row in range(1, len(data_list[index_data])):
            temp_list_date.append((names_list[index_row].split(" ")[0].replace('"', "").replace('=', ""),
                                   data_list[index_data][index_row]))
        result_dict[data_list[index_data][0]] = temp_list_date
    return result_dict


def parsing_portal_data(data_list: list):
    """
    Очищает фамилии от "" и =, преобразует строковое тип данных в int
    :param data_list: список списков строк
    :return: список кортежей (Фамилия, количество)
    """
    result_list = []
    for elem in data_list:
        result_list.append((elem[0].split(" ")[0].replace('"', "").replace('=', ""), int(elem[1])))
    return result_list
