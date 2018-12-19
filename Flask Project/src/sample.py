import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.style as style
# rc={'font.size': 32, 'axes.labelsize': 32, 'legend.fontsize': 32.0,
#     'axes.titlesize': 32, 'xtick.labelsize': 10, 'ytick.labelsize': 32}

# rc={'xtick.labelsize': 10}


def count_plt(parm):
    # style.use('seaborn-poster')
    sns.set_context('talk')
    df = pd.read_excel(r'file_docs\target_file.xlsx')
    sns.set_style("whitegrid")
    sns.set(rc={'xtick.labelsize': 8})
    # sns.set_style("ticks", {"xtick.major.size": 8, "ytick.major.size": 8})
    sns.countplot(x=parm, data=df,alpha=0.85,palette=("viridis_r"))
    # plt.xticks(rotation=90)
    # plt.set_xlabel('Project',size=6)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.show()
    # plt.savefig(rf"static\{parm.replace(' ', '_')}.png")


count_plt('Project Role Code')
