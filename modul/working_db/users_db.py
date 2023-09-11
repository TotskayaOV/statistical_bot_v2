from .data_base import DataBase


class User(DataBase):
    def __init__(self):
        super().__init__()

    def create_table_users(self):
        sql = '''CREATE TABLE IF NOT EXISTS users 
        (id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(50), status VARCHAR(50))'''
        self.execute(sql, commit=True)

    def create_table_users_contacts(self):
        sql = '''CREATE TABLE IF NOT EXISTS contacts_users 
        (fk_users INTEGER PRIMARY KEY, tg_id INTEGER, status_mail INTEGER DEFAULT 0)'''
        self.execute(sql, commit=True)

    def add_user(self, user_data: dict):
        parameters = (user_data.get('name'), user_data.get('status'))
        sql = '''INSERT INTO users (name, status) 
        VALUES (?, ?)'''
        self.execute(sql, parameters, commit=True)

    def add_contacts(self, contact_data: dict):
        parameters = (contact_data.get('fk_users'), contact_data.get('tg_id'), contact_data.get('status_mail'))
        sql = '''INSERT INTO contacts_users (fk_users, tg_id, status_mail) 
         VALUES (?, ?, ?)'''
        self.execute(sql, parameters, commit=True)

    def get_users(self):
        sql = '''SELECT * FROM users'''
        return self.execute(sql, fetchall=True)

    def get_contacts(self):
        sql = '''SELECT * FROM contacts_users'''
        return self.execute(sql, fetchall=True)

    def get_the(self, name_table: str, **kwargs):
        """
        Возвращает одну запись из таблиц пользователи или контакты
        :param name_table: users, contacts_users
        :param kwargs: tg_id
        :return:
        """
        sql = f'''SELECT * FROM {name_table} WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def get_for_middleware(self, **kwargs):
        sql = '''SELECT status FROM users JOIN contacts_users ON users.id == contacts_users.fk_users WHERE '''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        return self.execute(sql, parameters, fetchone=True)

    def update_user_name(self, new_data: dict):
        parameters = (new_data.get('name'), new_data.get('id'))
        sql = '''UPDATE users SET name=? WHERE id=? '''
        self.execute(sql, parameters, commit=True)

    def update_tg_id(self, new_data: dict):
        parameters = (new_data.get('tg id'), new_data.get('id'))
        sql = '''UPDATE contacts_users SET tg_id=? WHERE fk_users=? '''
        self.execute(sql, parameters, commit=True)

    def update_user_status(self, new_data: dict):
        parameters = (new_data.get('status'), new_data.get('id'))
        sql = '''UPDATE users SET status=? WHERE id=? '''
        self.execute(sql, parameters, commit=True)

    def update_mail_status(self, new_data: dict):
        parameters = (new_data.get('status'), new_data.get('id'))
        sql = '''UPDATE contacts_users SET status_mail=? WHERE fk_users=? '''
        self.execute(sql, parameters, commit=True)

    def remove_user(self, **kwargs):
        sql = '''DELETE FROM users WHERE id=?'''
        sql, parameters = self.extract_kwargs(sql, kwargs)
        self.execute(sql, parameters, commit=True)
