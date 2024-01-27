import pyodbc

from flask import Flask, render_template, request, url_for, flash

from werkzeug.middleware.proxy_fix import ProxyFix


app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app)




@app.route('/')
def ListRDV():
    server = '172.16.15.69'
    database = 'TESTMEDIC'
    username = 'sa'
    password = 'sa2014as'
    conn = pyodbc.connect(
        'DRIVER={SQL Server};SERVER=' + server + ';DATABASE=' + database + ';UID=' + username + ';PWD=' + password)
    cur= conn.execute("SELECT * FROM medic")
    patients = cur.fetchall()
    print(patients)
    return render_template('RDV.html', patients=patients)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8000, debug=True)