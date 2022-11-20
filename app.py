from flask import Flask, render_template, request
from flask_mysqldb import MySQL

app= Flask(__name__)

app.config['MYSQL_HOST']= 'root'
app.config['MYSQL_USER']= 'root'
app.config['MYSQL_PASSWORD']= 'root123'
app.config['MYSQL_DB']= 'my_users'

mysql=MySQL(app)

@app.route('/', methods= ['GET', 'POST'])
def index():
    if request.method == 'GET':
        details= request.form
        username= details['username']
        password= details['password']
        cur= mysql.connection.cursor()
        cur.execute("INSERT INTO users(username, password) VALUES (%s, %s)", (username, password))
        mysql.connection.commit()
        cur.close()
        return 'success'
    return render_template('index.html')    

if __name__ == '__main__':
    app.run()