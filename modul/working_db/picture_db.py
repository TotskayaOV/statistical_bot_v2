from .data_base import DataBase
from datetime import datetime


class Picture(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_reports(self):
        sql = '''CREATE TABLE IF NOT EXISTS reports 
        (id_repo TEXT PRIMARY KEY, date_point TEXT, url_str TEXT)'''
        self.execute(sql, commit=True)


    def add_reports(self, user_data: dict):
        parameters = (user_data.get('id_repo'), str(datetime.now().date()), user_data.get('url_str'))
        sql = '''INSERT INTO reports (id_repo, date_point, url_str) 
        VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_reports(self, **kwargs):
        sql = f'''SELECT * FROM reports WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        result_db = self.execute(sql, parameters, fetchone=True)
        if result_db:
            date_obj = datetime.strptime(result_db[1], '%Y-%m-%d')
            delta = datetime.now().date() - date_obj.date()
            if delta.days < 2:
                return result_db
            else:
                self.remove_reports(id_repo=result_db[0])


    def get_stat_reports(self, **kwargs):
        sql = f'''SELECT url_str FROM reports WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def remove_reports(self, **kwargs):
        sql = f'''DELETE FROM reports WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)