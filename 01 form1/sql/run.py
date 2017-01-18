from flask import Flask, render_template, request
import MySQLdb

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.errorhandler(404)
def page_not_found(e):
    return "YIKEDS!!!"

@app.route('/enternew/')
def new_student():
    return render_template('student.html')

@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            nm = request.form['nm']
            addr = request.form['add']
            city = request.form['city']
            pin = request.form['pin']
            db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                                 user="root",  # your username
                                 passwd="password",  # your password
                                 db="pythonprogramming")  # name of the data base

            cur = db.cursor()

            cur.execute("INSERT INTO students VALUES (NULL,%s,%s,%s)",(addr,city,pin))

            db.commit()
            msg = "Record successfully added"
        except Exception as e:
            print(e)
            db.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/list')
def list():
    db = MySQLdb.connect(host="localhost",  # your host, usually localhost
                         user="root",  # your username
                         passwd="password",  # your password
                         db="pythonprogramming")  # name of the data base

    cur = db.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();

    return render_template("list.html", rows=rows)

if __name__ == '__main__':
    app.run(debug=True)