import polars as pl

from loader import user_db, jira_db
from .modification_string import string_with_dates
from .creating_graphs import created_bar
from .conversion_human_form import conversion_standard_timestamp



def round_float(num):
    return round(num * 100, 2)

def assembling_data_frame(name_table: str, date_dict=None, date_obj=None, user_target=False) -> pl.DataFrame:
    """
    Функция собирает данные по заданным параметрам в датафрейм
    :param name_table: источник данных
    :param date_dict: словарь с началом и концо периода
    :param date_obj: дата данных
    :param user_target: персонализированный запрос
    :return: (общий показатель всего отдела, дата фрейм всего отдела /, дата фрейм по персонализации)
    """
    users_data = user_db.get_users()
    df_users = pl.DataFrame({'index': [elem[0] for elem in users_data], 'name': [elem[1] for elem in users_data]})
    if date_dict:
        result_bd = jira_db.get_period_jira(name_table, date_dict)
    else:
        result_bd = jira_db.get_jira(name_table, date_wd=date_obj)
    df = pl.DataFrame({'date': [elem[1] for elem in result_bd],
                       'index': [elem[2] for elem in result_bd],
                       'values': [elem[3] for elem in result_bd]})
    if df.is_empty():
        return False
    else:
        cnt_values = df['values'].sum()
        if date_dict:
            df = df.join(df_users, on='index', how='inner').sort('date')
        else:
            df = df.join(df_users, on='index', how='inner').sort('values', descending=True)
        df = df.drop('index')
        match name_table:
            case 'j_sla':
                df = df.with_columns([((df.select(pl.col('values') * 100)).to_series(0)).alias('values')])
                cnt_values = df['values'].mean()
            case 'j_times':
                df = df.with_columns([(df.select(pl.col('values')).to_series(0).round(2)).alias('values')])
                cnt_values = df['values'].mean()
        if user_target:
            return (cnt_values, df, df.filter(pl.col('name') == user_target))
        else:
            return (cnt_values, df)


# def create_period(table_name, date_dict, user_target=False):
#     initial_df = assembling_data_frame(table_name, date_dict=date_dict)
#     df_date = initial_df.groupby('date').sum().sort('date')
#     df_date = df_date.drop('name')
#     df_name = initial_df.groupby('name').sum().sort('values', descending=True)
#     df_name = df_name.drop('date')
#     # personalized_data_period('Айрапетян', {'date_in': '2023-06-18', 'date_on': '2023-06-26'})
#     return {'dict_date': df_date.to_dicts(), 'dict_name': df_name.to_dicts()}
#     # string_with_dates(df_date.to_dicts(),'time')

def create_one_day(table_name, date_obj, user_target=False):
    if user_target:
        initial_tuple = assembling_data_frame(table_name, date_obj=date_obj, user_target=user_target)
        if initial_tuple:
            return (initial_tuple[0], initial_tuple[1], initial_tuple[2].to_dicts())
    else:
        initial_tuple = assembling_data_frame(table_name, date_obj=date_obj)
        if initial_tuple:
            return (initial_tuple[0], initial_tuple[1], initial_tuple[1].to_dicts())


def personalized_data_period(table_name: str, date_dict: dict, name_user: str):
    data_tuple = assembling_data_frame(table_name, date_dict=date_dict)
    if data_tuple:
        df = data_tuple[1]
        df_filter = df.filter(pl.col('name') == name_user).drop('name')
        match table_name:
            case 'j_sla':
                df_total = df.groupby(pl.col('date')).agg(pl.col('values').mean().alias("total"))
            case 'j_times':
                df_total = df.groupby(pl.col('date')).agg(pl.col('values').mean().alias("total"))
            case _:
                df_total = df.groupby(pl.col('date')).agg(pl.col('values').sum().alias("total"))
        df_filter = df_filter.join(df_total, on="date").sort('date', descending=True)
        return (df_filter, df_filter.to_dicts())
    else:
        return False
