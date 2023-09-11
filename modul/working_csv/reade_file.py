import csv


def read_csv_file(path: str, encoding: str, num_row: int, delimiter: str)  -> list:
    '''
    чтение файла
    :param path: путь к файлу
    :param encoding: кодировка
    :param num_row: с какой строки читать файл
    :param delimiter: разделитель
    :return: [[], []]
    '''
    db_list = []
    with open(path, 'r', encoding=encoding) as file:
        csv_reader = csv.reader(file, delimiter=delimiter, quoting=csv.QUOTE_ALL)
        for line_num, row in enumerate(csv_reader):
            if line_num >= num_row:  # Пропуск первых двух строк
                db_list.append(row)
        return db_list