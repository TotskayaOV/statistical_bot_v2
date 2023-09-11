import matplotlib.pyplot as plt
import mplcyberpunk
from .conversion_human_form import conversion_standard_timestamp

from config import left_colors, right_colors



def addlabels(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, y[i], ha = 'center', fontsize='x-small')

def addlabels_2(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, conversion_standard_timestamp(y[i])[-5:], ha = 'center', fontsize='x-small',
                 bbox = dict(facecolor = 'black', alpha = .5))

def addlabels_SLA(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2, round(y[i], 1), ha = 'center', fontsize='x-small',
                 bbox = dict(facecolor = 'black', alpha = .5))

def addlabels2(x,y):
    for i in range(len(x)):
        plt.text(i, y[i]//2,y[i], ha = 'center',
                 bbox = dict(facecolor = 'black', alpha = .5))

def addlabels3(x, y, max_y):
    for i in range(len(x)):
        plt.text(i, max_y, y[i], ha = 'center',
                 bbox = dict(facecolor = 'black', alpha = .5))

def addlabels_3(x, y, max_y):
    for i in range(len(x)):
        print(conversion_standard_timestamp(y[i]))
        plt.text(i, max_y, conversion_standard_timestamp(y[i])[-5:], ha = 'center',
                 bbox = dict(facecolor = 'black', alpha = .5))

def addlabels3_SLA(x, y, max_y):
    for i in range(len(x)):
        plt.text(i, max_y, round(y[i], 1), ha = 'center',
                 bbox = dict(facecolor = 'black', alpha = .5))

def created_bar_name(df: object, t_label: str, file_name: str, right_position=False) -> int:
    """
    :return: integer:
                1 - файл с данными создан
                0 - данных за дату нет
    """
    try:
        plt.style.use("cyberpunk")
        fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
        bars = ax.bar(df['name'], df['values'], color=left_colors, zorder=2)
        plt.xticks(rotation=90)
        if right_position:
            ax.yaxis.set_label_position("right")
            ax.yaxis.tick_right()
            plt.title(t_label, fontsize=17, loc='right')
        else:
            plt.title(t_label, fontsize=17, loc='left')
        if 'j_times' in file_name:
            addlabels_2(df['name'], df['values'])
        else:
            addlabels(df['name'], df['values'])
        mplcyberpunk.add_bar_gradient(bars=bars)
        plt.savefig(f'./cred/{file_name}.jpg')
        plt.close('all')
        return 1
    except:
        return 0


def created_bar(df: object, t_label: str, file_name: str, right_position=False) -> int:
    """
    :return: integer:
                1 - файл с данными создан
                0 - данных за дату нет
    """
    try:
        plt.style.use("cyberpunk")
        fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
        bars = ax.bar(df['date'], df['values'], color=left_colors, zorder=2)
        bars1 = ax.bar(df['date'], df['total'], color='beige', zorder=1)
        plt.xticks(rotation=45)
        if right_position:
            ax.yaxis.set_label_position("right")
            ax.yaxis.tick_right()
            plt.title(t_label, fontsize=17, loc='right')
        else:
            plt.title(t_label, fontsize=17, loc='left')
        if 'j_times' in file_name:
            addlabels_2(df['date'], df['values'])
            addlabels_3(df['date'], df['total'], df['total'].max())
        elif 'j_sla' in file_name:
            addlabels_SLA(df['date'], df['values'])
            addlabels3_SLA(df['date'], df['total'], df['total'].max())
        else:
            addlabels2(df['date'], df['values'])
            addlabels3(df['date'], df['total'], df['total'].max())
        mplcyberpunk.add_bar_gradient(bars=bars)
        mplcyberpunk.add_bar_gradient(bars=bars1)
        plt.savefig(f'./cred/{file_name}.jpg')
        plt.close('all')
        return 1
    except:
        return 0

def horizontal_bar(df: object, t_label: str, file_name: str, right_position=False) -> int:
    try:
        plt.style.use("cyberpunk")
        fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
        bars = ax.barh(df['name'], df['values'], color='green', zorder=2)
        bars1 = ax.barh(df['name'], 100, color='orange', zorder=2)
        plt.xticks(rotation=90)
        plt.title('SLA', fontsize=17)
        mplcyberpunk.add_bar_gradient(bars=bars1)
        mplcyberpunk.add_bar_gradient(bars=bars)
        plt.savefig(f'./cred/{file_name}.jpg')
        plt.close('all')
        return 1
    except:
        return 0
#
# def general_pie_graf(date_obj: str):
#     data_request = db.get_general(date=datetime.strptime(date_obj, '%Y-%m-%d'))
#     data_request_portal = db.get_date_portal(date=datetime.strptime(date_obj, '%Y-%m-%d'))
#     if data_request and data_request_portal:
#         pl_request = pl.DataFrame({
#             'new': [row[1] for row in data_request],
#             'fast': [row[2] for row in data_request],
#             'all':  pl.Series([row[3] for row in data_request_portal]).sum()
#         })
#         plt.style.use("cyberpunk")
#         fig, ax = plt.subplots(figsize=(5, 5), layout='constrained')
#         size = 0.2
#         vals = np.array([[pl_request.item(0, 'new'), pl_request.item(0, 'new') - pl_request.item(0, 'fast')],
#                          [pl_request.item(0, 'all') - pl_request.item(0, 'new'), 0]])
#         outer_colors = ['darkgreen', 'darkgreen']
#         inner_colors = ['green', 'lime', 'darkgreen', 'darkgreen']
#         ax.pie(vals.sum(axis=1), radius=1, colors=outer_colors,
#                wedgeprops=dict(width=size, edgecolor='darkgreen'))
#         ax.pie(vals.flatten(), radius=1 - size, colors=inner_colors,
#                wedgeprops=dict(width=size, edgecolor='darkgreen'))
#         ax.set(aspect="equal", title=f"Всего проверок анкет: {pl_request.item(0, 'all')}\n"
#                         f"Новых анкет: {pl_request.item(0, 'new')}\n"
#                        f"Проверено за 15 минут: {pl_request.item(0, 'fast')}")
#         plt.savefig(f'./cred/general-{date_obj}.jpg')
#         plt.close('all')
#         return 1
#     else:
#         return 0