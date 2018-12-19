import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from flask import Flask, render_template, request

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'file_docs\\')


# def count_plt(parm):
#     df = pd.read_excel(r'file_docs\target_file.xlsx')
#     fig = df.groupby(parm).count()['Employee Code'].plot.bar().get_figure()
#     fig.savefig(rf"static\{parm.replace(' ', '_')}.png", bbox_inches='tight')


def count_plt(parm):
    df = pd.read_excel(r'file_docs\target_file.xlsx')
    # sns.set_context('talk')
    sns.set_style("whitegrid")
    sns.set(rc={'xtick.labelsize': 8})
    sns.countplot(x=parm, data=df,palette=("viridis_r"),alpha=0.85)
    plt.gcf().autofmt_xdate()
    plt.tight_layout()
    plt.savefig(rf"static\{parm.replace(' ', '_')}.png")


def col_list(file):
    df = pd.read_excel(file)
    return list(df.columns)


def del_files(folder):
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
    if request.files and request.method == 'POST':
        if not os.path.isdir(target):
            os.mkdir(target)
        file = request.files.get("file")
        file.save('\\'.join([target, 'target_file.xlsx']))
        labels = col_list(file)
        return render_template("index.html", labels=labels)
    elif request.method == 'POST':
        del_files('static')
        plot = request.form['plot']
        print('Plot ' + plot)
        if plot == 'Count plot':
            parms = request.form.getlist('parm[]')
            for parm in parms:
                count_plt(parm)
            # del_files('file_docs')
            return render_template("output.html", results=os.listdir('static'))
        else:
            return 'Plot not available'


if __name__ == "__main__":
    app.run(host='127.0.0.69', port='99', debug=True)
    del_files('static')
    del_files('file_docs')
