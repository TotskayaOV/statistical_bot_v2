from .data_base import DataBase


class Portal(DataBase):
    def __init__(self):
        super().__init__()

    def create_general_data(self):
        sql = '''CREATE TABLE IF NOT EXISTS general_data 
        (date_wd DATE PRIMARY KEY, count_new_user INTEGER, fast_verif INTEGER)'''
        self.execute(sql, commit=True)

    def create_table_portal(self):
        sql = '''CREATE TABLE IF NOT EXISTS general_portal 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, date_wd DATE,
         user_id INTEGER, count_verify INTEGER)'''
        self.execute(sql, commit=True)

    def add_portal(self, portal_data: dict):
        parameters = (portal_data.get('date_wd'), portal_data.get('user_id'), portal_data.get('value'))
        sql = '''INSERT INTO general_portal (date_wd, user_id, count_verify) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def add_general_data(self, new_data: dict):
        parameters = (new_data.get('date_wd'), new_data.get('count_new_user'), new_data.get('fast_verif'))
        sql = '''INSERT INTO general_data (date_wd, count_new_user, fast_verif) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_portal(self, name_table: str, **kwargs):
        """
        Получить данные Портал
        :param name_table: general_portal, general_data
        :param kwargs: date_wd, user_id
        :return: list[tuple, ]
        """
        sql = f'''SELECT * FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def update_portal(self, name_table: str, name_col, new_data: dict):
        """
        Обновляет таблицы портал
        :param new_data: dict{value: str, id: int}
        :param name_table:  general_portal
        :param name_col: count_verify
        """
        parameters = (new_data.get('value'), new_data.get('id'))
        sql = f'''UPDATE {name_table} SET {name_col}=? WHERE id=? '''
        self.execute(sql, parameters, commit=True)

    def update_general_data(self, new_data: dict):
        parameters = (new_data.get('count_new_user'), new_data.get('fast_verif'), new_data.get('date_wd'))
        sql = f'''UPDATE general_data SET count_new_user=? 
        AND fast_verif=? WHERE date_wd=? '''
        self.execute(sql, parameters, commit=True)

    def remove_portal(self, name_table: str, **kwargs):
        """
        Удаляет данные из таблицы Портала
        :param name_table: general_portal, general_data
        :param kwargs: date_wd, user_id
        """
        sql = f'''DELETE FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)
