from .data_base import DataBase


class Technical(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_delimiters(self):
        sql = '''CREATE TABLE IF NOT EXISTS delimiters 
        (files_name VARCHAR(25) PRIMARY KEY, simbol_delimiter VARCHAR(25))'''
        self.execute(sql, commit=True)

    def create_table_datetime(self):
        sql = '''CREATE TABLE IF NOT EXISTS date_str 
        (files_name VARCHAR(25) PRIMARY KEY, simbol_datetime VARCHAR(25))'''
        self.execute(sql, commit=True)

    def create_table_number_row(self):
        sql = '''CREATE TABLE IF NOT EXISTS numbers_start_row 
        (files_name VARCHAR(25) PRIMARY KEY, num_row INTEGER)'''
        self.execute(sql, commit=True)

    def add_delimiters(self, user_data: dict):
        parameters = (user_data.get('files_name'), user_data.get('simbol_delimiter'))
        sql = '''INSERT INTO delimiters (files_name, simbol_delimiter) 
        VALUES (?, ?)'''
        self.execute(sql, parameters, commit=True)

    def add_datetime(self, user_data: dict):
        parameters = (user_data.get('files_name'), user_data.get('simbol_datetime'))
        sql = '''INSERT INTO date_str (files_name, simbol_datetime) 
        VALUES (?, ?)'''
        self.execute(sql, parameters, commit=True)

    def add_number_row(self, user_data: dict):
        parameters = (user_data.get('files_name'), user_data.get('num_row'))
        sql = '''INSERT INTO numbers_start_row (files_name, num_row) 
        VALUES (?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_delimiters(self, **kwargs):
        sql = f'''SELECT simbol_delimiter FROM delimiters WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def get_datetime(self, **kwargs):
        sql = f'''SELECT simbol_datetime FROM date_str WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def get_numbers_start_row(self, **kwargs):
        sql = f'''SELECT num_row FROM numbers_start_row WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def get_all(self, name_table: str):
        """
        Возвращает одну запись из таблиц пользователи или контакты
        :param name_table: delimiters, date_str, numbers_start_row
        :param kwargs: files_name
        :return:
        """
        sql = f'''SELECT * FROM {name_table}'''
        return self.execute(sql, fetchall=True)

    def update_delimiters(self, new_data: dict):
        parameters = (new_data.get('simbol_delimiter'), new_data.get('files_name'))
        sql = '''UPDATE delimiters SET simbol_delimiter=? WHERE files_name=? '''
        self.execute(sql, parameters, commit=True)

    def update_datetime(self, new_data: dict):
        parameters = (new_data.get('simbol_datetime'), new_data.get('files_name'))
        sql = '''UPDATE date_str SET simbol_datetime=? WHERE files_name=? '''
        self.execute(sql, parameters, commit=True)

    def update_numbers_start_row(self, new_data: dict):
        parameters = (new_data.get('num_row'), new_data.get('files_name'))
        sql = '''UPDATE numbers_start_row SET num_row=? WHERE files_name=? '''
        self.execute(sql, parameters, commit=True)

    def remove_user(self, name_table: str, **kwargs):
        sql = f'''DELETE FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)