from .conversion_human_form import conversion_standard_timestamp


def string_with_dates(raw_list: list, data_type: str) -> tuple:
    result_string = ''
    cnt_values = 0
    for dict_elem in raw_list:
        match data_type:
            case 'quantity':
                result_string += dict_elem.get('date') + ': ' + str(dict_elem.get('values')) + '\n'
                cnt_values += dict_elem.get('values')
            case 'time':
                result_string += dict_elem.get('date') + ': ' + conversion_standard_timestamp(dict_elem.get('values'))\
                                 + '\n'
                cnt_values += dict_elem.get('values')
            case 'percent':
                result_string += dict_elem.get('date') + ': ' + str(round((dict_elem.get('values') * 100), 2)) \
                                 + '%\n'
                cnt_values += dict_elem.get('values')
    match data_type:
        case 'time': cnt_values = conversion_standard_timestamp(cnt_values/len(raw_list))
        case 'percent': cnt_values = round(cnt_values/len(raw_list) * 100, 2)
    return (cnt_values, result_string)


def string_with_names(raw_list: list, data_type: str) -> tuple:
    result_string = ''
    cnt_values = 0
    for dict_elem in raw_list:
        match data_type:
            case 'quantity':
                result_string += dict_elem.get('name') + ': ' + str(dict_elem.get('values')) + '\n'
                cnt_values += dict_elem.get('values')
            case 'time':
                result_string += dict_elem.get('name') + ': ' + conversion_standard_timestamp(dict_elem.get('values')) \
                                 + '\n'
                cnt_values += dict_elem.get('values')
            case 'percent':
                result_string += dict_elem.get('date') + ': ' + str(round((dict_elem.get('values') * 100), 2)) \
                                 + '%\n'
                cnt_values += dict_elem.get('values')
    match data_type:
        case 'time':
            cnt_values = conversion_standard_timestamp(cnt_values / len(raw_list))
        case 'percent':
            cnt_values = round(cnt_values / len(raw_list) * 100, 2)
    return (cnt_values, result_string)