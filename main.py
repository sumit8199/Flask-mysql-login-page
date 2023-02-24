# This is a sample Python script.


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from flask import Flask, render_template, request
import mysql.connector





app = Flask(__name__)


conn = mysql.connector.connect(host = "localhost", username = "root", password='', database='login2')
cursor=conn.cursor()

@app.route('/')
def hello():
    return render_template('login1.html')


@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/home.html', methods=['GET', 'POST'])
def login_validation():
    username= request.form.get('username')
    password = request.form.get('password')

    cursor.execute("""SELECT * FROM `loginform` WHERE `username` LIKE '{}' AND `password` LIKE '{}'""".format(username, password))
    users = cursor.fetchall()
    if len(users) > 0:
        return render_template('home.html')
    else:
        return render_template('login1.html')


@app.route('/register.html', methods=['GET', 'POST'])
def register():
    email = request.form.get('email')
    username= request.form.get('username')
    password = request.form.get('password')

    cursor.execute("""INSERT INTO `loginform` (`username`,`email`,`password`) VALUES (NULL,'{}','{}','{}')""".format(username, email, password))
    conn.commit()
    return "user registered successfully"


if __name__ == "__main__":
    app.run(debug=True)
