from flask import render_template, request
from . import app, APP_ROOT
import os
from .utilityFuncs import col_list, count_plt, del_files

static_path = os.path.join(APP_ROOT, 'static')


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/upload", methods=['POST'])
def upload():
    if request.method == 'POST' and not request.form:
        file = request.files.get("file")
        labels = col_list(file)
        return render_template("index.html", labels=labels)
    elif request.method == 'POST' and len(request.form['plot']) > 1:
        del_files(static_path)
        plot = request.form['plot']
        if plot == 'Count plot':
            parms = request.form.getlist('parm[]')
            for parm in parms:
                count_plt(parm)

            return render_template("output.html", results=os.listdir(static_path))
        else:
            return 'Plot not available'
