import os, pandas as pd, matplotlib.pyplot as plt
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'file_docs\\')

def count_plt(parm):
    df = pd.read_excel(r'file_docs\target_file.xlsx')
    fig = df.groupby(parm).count()['Employee Code'].plot.bar().get_figure()
    fig.savefig(r"static\output.png", bbox_inches='tight')


def col_list(file):
    df = pd.read_excel(file)
    return list(df.columns)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
    if request.files and request.method == 'POST':
        print(1)
        if not os.path.isdir(target):
            os.mkdir(target)
        file = request.files.get("file")
        file.save('\\'.join([target,'target_file.xlsx']))
        labels = col_list(file)
        return render_template("index.html",labels=labels)
    elif request.method == 'POST':
        print(2)
        plot = request.form['plot']
        print('Plot' + plot)
        if plot == 'Count plot':
            parm = request.form['parm']
            print(parm)
            count_plt(parm)
            return render_template("output.html", user_image=r'static\output.png')
        else:
            return 'Plot not available'


if __name__ == "__main__":
    app.run(host='127.0.0.91',port='98',debug=True)
