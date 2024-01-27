import pyodbc

from flask import Flask, render_template, request, url_for, flash

from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)

server = '172.16.15.69'
database = 'SIHRDV'
username = 'sa'
password = 'sa2014as'


@app.route('/', methods=["GET", "POST"])
def ListRDV():
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur= conn.execute("SELECT * FROM RDV")
    patients = cur.fetchall()
    print(patients)
    if request.method == "POST":
        data = dict(request.form)
        patients = getRDV(data["search"])
    else:
        print("Aucun résultat")
    return render_template('RDV.html', patients=patients)

@app.route('/rdv')
def getRDV(search):
    conn = pyodbc.connect('DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur = conn.execute("SELECT * FROM RDV  WHERE EXAMEN  LIKE ? OR SERVICE   LIKE ?", ("%"+search+"%", "%"+search+"%",))
    patients = cur.fetchall()
    print(patients)
    return render_template('RDV.html', patients=patients)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)