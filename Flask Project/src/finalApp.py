import os, mpld3, pandas as pd, matplotlib.pyplot as plt
from flask import Flask, render_template, request, url_for, redirect, send_file

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


def func(file, x, y):
    df = pd.read_excel(file)
    # plt.figure(figsize=(10, 8))
    fig = df.groupby('Project Role Name').count()['Employee Code'].plot.bar().get_figure()
    # fig = df.groupby(x).count()[y].plot.bar().get_figure()
    # plt.tight_layout()
    # outfile = APP_ROOT + r'\templates\out.html'
    # mpld3.save_html(fig, open(outfile, 'w'))
    # mpld3.show()
    fig.savefig(r"static\output.png", bbox_inches='tight')

def col_list(file):
    df = pd.read_excel(file)
    labels = list(df.columns)
    render_template("upload.html", labels=labels)

@app.route("/")
def index():
    return render_template("upload.html")

@app.route("/upload", methods=['POST'])
def upload():
    file = request.files.get("file")
    # xparam = request.form.get("parm1")
    # yparam = request.form.get("parm2")
    # df = pd.read_excel(file)
    # labels = list(df.columns)
    # render_template("upload.html", labels=labels)
    func(file, 1, 1)
    # func(file, xparam, yparam)
    # return render_template("out.html")
    # return redirect(request.referrer or url_for('index'))
    return render_template("output.html", img = 'output.png')



if __name__ == "__main__":
    app.run(debug=True)
