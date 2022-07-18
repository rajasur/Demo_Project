import os
from flaskext.mysql import MySQL
from flask import jsonify, request, render_template, Flask
import pymysql
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = "root"
#app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv("db_root_password")
app.config["MYSQL_DATABASE_PASSWORD"] = "Ahcc@12345"
app.config["MYSQL_DATABASE_DB"] = os.getenv("db_name")
app.config["MYSQL_DATABASE_HOST"] = os.getenv("MYSQL_SERVICE_HOST")
app.config["MYSQL_DATABASE_PORT"] = 3306
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
#print(cursor)
cursor.execute("USE food")
#cursor = conn.cursor(pymysql.cursors.DictCursor)
cursor.execute("SELECT * FROM Food")
for i in cursor.fetchall():
    print(i[0])
cur = mysql.connect.cursor()

for i in cur.execute("""SELECT * FROM Food"""):
    print(i)

'''def ConnectionString():
    driver='{SQL Server Native Client 11.0}'
    server='W-PF3MLQY4\SQLEXPRESS'
    database='Food'
    username='assignment'
    password='Ahcc@12345'
    connection_string="DRIVER="+driver+";SERVER="+server+";DATABASE="+database+";UID="+username+";PWD="+password
    return connection_string'''
    