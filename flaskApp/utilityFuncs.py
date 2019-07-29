import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
from . import APP_ROOT

df = pd.DataFrame()


def create_df(file):
    global df
    df = pd.read_excel(file)


def col_list(file):
    global df
    create_df(file)
    return list(df.columns)


def count_plt(parm):
    print(APP_ROOT)
    print(os.path.join(
        APP_ROOT, "static\\{}.png".format(parm.replace(' ', '_'))), -------2)
    global df
    sns.set_style("whitegrid")
    sns.set(rc={'xtick.labelsize': 8})
    sns.countplot(x=parm, data=df, palette=("viridis_r"), alpha=0.85)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    # print("static\\{}.png".format(parm.replace(' ', '_')))
    plt.savefig(os.path.join(
        APP_ROOT, r"static\\{}.png".format(parm.replace(' ', '_'))))
    # plt.savefig(r"\\static\\{parm.replace(' ', '_')}.png")


def del_files(folder):
    print(os.path.join(APP_ROOT, folder), ------1)
    for the_file in os.listdir(os.path.join(APP_ROOT, folder)):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)
