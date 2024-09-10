from idlelib.macosx import addOpenEventSupport

from flask import Flask, jsonify
from flask_mysqldb import MySQL

app = Flask(__name__)

app.config['MYSQL_HOST']='localhost'
app.config['MYSQL_PORT']=3306
app.config['MYSQL_USER']='root'
app.config['MYSQL_PASSWORD']='1234'
app.config['MYSQL_DB']='pucaronas'

mysql = MySQL(app)

@app.route('/getAlunos')
def getAlunos():  # put application's code here
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM aluno")
    data = cur.fetchall()
    cur.close()
    return jsonify(data)



@app.route('/')
def fuck():
    return 'Fuck'



if __name__ == '__main__':
    app.run()
