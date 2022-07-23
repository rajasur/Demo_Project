import os
from flaskext.mysql import MySQL
from flask import jsonify, request, render_template, Flask
import pymysql
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = os.getenv('MYSQL_ROOT_USER', 'root')
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv('db_root_password','admin')
app.config["MYSQL_DATABASE_DB"] = os.getenv('db_name')
app.config["MYSQL_DATABASE_HOST"] = os.getenv('MYSQL_SERVICE_HOST','localhost')
app.config["MYSQL_DATABASE_PORT"] = os.getenv('MYSQL_SERVICE_PORT','3306')
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
@app.route('/')
def hello_world():
    return render_template('home.html')

@app.route('/submit',methods=['GET','POST'])
def create():
    if request.method=="POST":   
        pi=int(request.form['pincode'])
        fr=str(request.form['fruit'])
        vg=str(request.form['vegetable'])
        cursor.execute("USE food")
        cursor.execute("INSERT INTO food (Pincode,Fruit_Name,Vegitable_Name) VALUES (%s,%s,%s)",(pi,fr,vg))
        conn.commit()    
        return render_template('searching.html')
    
@app.route('/display',methods=['GET','POSt'])
def Searching():
    if request.method=='POST':
        spincode=int(request.form['spincode'])
        svegetable=str(request.form['svegetable'])
        sfruit=str(request.form['sfruit'])
    d=dict()
    l=list()
    cursor.execute("USE food")
    cursor.execute("SELECT *FROM food")
    for i in cursor.fetchall():
        if (str(i[1])==sfruit) or (str(i[2])== svegetable) or (i[0]==spincode):
            d['Pincde']=i[0]
            d['Fruits_Name']=i[1]
            d['Vegetables_Name']=i[2]
            l.append(d)      
    return render_template('searching.html',val=l)
            

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)