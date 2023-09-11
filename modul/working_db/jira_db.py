from .data_base import DataBase


class Jira(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_jira_count(self):
        sql = '''CREATE TABLE IF NOT EXISTS j_counts 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, date_wd DATE,
         user_id INTEGER, count_task INTEGER)'''
        self.execute(sql, commit=True)

    def create_table_jira_time(self):
        sql = '''CREATE TABLE IF NOT EXISTS j_times 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, date_wd DATE,
         user_id INTEGER, time_task INTEGER)'''
        self.execute(sql, commit=True)

    def create_table_jira_sla(self):
        sql = '''CREATE TABLE IF NOT EXISTS j_sla 
        (id INTEGER PRIMARY KEY AUTOINCREMENT,
         date_wd DATE, user_id INTEGER, sla_task INTEGER)'''
        self.execute(sql, commit=True)

    def add_jira_count(self, jira_data: dict):
        parameters = (jira_data.get('date_wd'), jira_data.get('user_id'), jira_data.get('value'))
        sql = '''INSERT INTO j_counts (date_wd, user_id, count_task) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def add_jira_time(self, jira_data: dict):
        parameters = (jira_data.get('date_wd'), jira_data.get('user_id'), jira_data.get('value'))
        sql = '''INSERT INTO j_times (date_wd, user_id, time_task) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def add_jira_sla(self, jira_data: dict):
        parameters = (jira_data.get('date_wd'), jira_data.get('user_id'), jira_data.get('value'))
        sql = '''INSERT INTO j_sla (date_wd, user_id, sla_task) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_jira(self, name_table: str, **kwargs):
        """
        Получить данные Jira
        :param name_table: j_counts, j_times, j_sla
        :param kwargs: count_task, time_task, sla_task, date_wd, user_id
        :return: list[tuple, ]
        """
        sql = f'''SELECT * FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchall=True)

    def get_period_jira(self, name_table: str, jira_data: dict):
        parameters = (jira_data.get('date_in'), jira_data.get('date_on'))
        sql = f'''SELECT * FROM {name_table} WHERE date_wd BETWEEN ? AND ?'''
        return self.execute(sql, parameters, fetchall=True)


    def update_jira(self, name_table: str, name_col, new_data: dict):
        """
        Обновляет таблицы JIRA
        :param new_data: dict{value: str, id: int}
        :param name_table:  j_counts, j_times, j_sla
        :param name_col: count_task, time_task, sla_task
        """
        parameters = (new_data.get('value'), new_data.get('id'))
        sql = f'''UPDATE {name_table} SET {name_col}=? WHERE id=? '''
        self.execute(sql, parameters, commit=True)

    def remove_jira(self, name_table: str, **kwargs):
        """
        Удаляет данные из таблицы Jira
        :param name_table: j_counts, j_times, j_sla
        :param kwargs: date_wd, user_id
        """
        print(name_table, kwargs)
        sql = f'''DELETE FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)
