from flask import Flask, render_template, request
import psycopg2

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
            db = psycopg2.connect(database="crawldashboard", user="postgres", password="postgres@123", host="127.0.0.1", port="5432")  # name of the data base

            cur = db.cursor()

            cur.execute("INSERT INTO students VALUES (%s,%s,%s,%s)",(nm,city,addr,pin))

            db.commit()
            msg = "Record successfully added"
        except Exception as e:
            print(e)
            db.rollback()
            msg = "error in insert operation"

        finally:
            return render_template("result.html", msg=msg)
            db.close()


@app.route('/list')
def list():
    db = psycopg2.connect(database="crawldashboard", user="postgres", password="postgres@123", host="127.0.0.1", port="5432")

    cur = db.cursor()
    cur.execute("select * from students")

    rows = cur.fetchall();
    print rows

    return render_template("list.html", rows=rows)

if __name__ == '__main__':
    app.run(host= '10.10.5.101', port=9000,debug=True)