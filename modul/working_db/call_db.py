from .data_base import DataBase


class Call(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_calls(self):
        sql = '''CREATE TABLE IF NOT EXISTS calls 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, date_wd DATE,
         user_id INTEGER, count_call INTEGER)'''
        self.execute(sql, commit=True)

    def add_call(self, call_data: dict):
        parameters = (call_data.get('date_wd'), call_data.get('user_id'), call_data.get('value'))
        sql = '''INSERT INTO calls (date_wd, user_id, count_call) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_call(self, name_table: str, **kwargs):
        """
        Получить данные Портал
        :param name_table: calls
        :param kwargs: date_wd, user_id
        :return: list[tuple, ]
        """
        sql = f'''SELECT * FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def update_call(self, name_table: str, name_col, new_data: dict):
        """
        Обновляет таблицы портал
        :param new_data: dict{value: str, id: int}
        :param name_table:  calls
        :param name_col: count_call
        """
        parameters = (new_data.get('value'), new_data.get('id'))
        sql = f'''UPDATE {name_table} SET {name_col}=? WHERE id=? '''
        self.execute(sql, parameters, commit=True)

    def remove_call(self, name_table: str, **kwargs):
        """
        Удаляет данные из таблицы Портала
        :param name_table: calls
        :param kwargs: date_wd, user_id
        """
        sql = f'''DELETE FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)
