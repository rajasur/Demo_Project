import os
from flaskext.mysql import MySQL
from flask import jsonify, request, render_template, Flask
import pymysql
app = Flask(__name__)

mysql = MySQL()

# MySQL Local configurations
'''
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = 'Ahcc@12345'
app.config['MYSQL_DATABASE_DB'] = 'Food'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config["MYSQL_DATABASE_PORT"] = 3306
'''
# MySQL configurations
app.config["MYSQL_DATABASE_USER"] = os.getenv('MYSQL_ROOT_USER', 'root')
app.config["MYSQL_DATABASE_PASSWORD"] = os.getenv('db_root_password','admin')
app.config["MYSQL_DATABASE_DB"] = os.getenv('db_name')
app.config["MYSQL_DATABASE_HOST"] = os.getenv('MYSQL_SERVICE_HOST','localhost')
app.config["MYSQL_DATABASE_PORT"] = int(os.getenv('MYSQL_SERVICE_PORT','3306'))
mysql.init_app(app)
conn = mysql.connect()
cursor = conn.cursor()
@app.route('/')
def hello_world():
    return render_template('default.html')

@app.route('/submit',methods=['GET','POST'])
def create(): 
    if request.method=="POST":   
        pi=int(request.form['pincode'])
        fr=str(request.form['fruit'])
        vg=str(request.form['vegetable'])
        cursor.execute("USE Food")
        cursor.execute("INSERT INTO food (Pincode,Fruit_Name,Vegitable_Name) VALUES (%s,%s,%s)",(pi,fr,vg))
        conn.commit()    
        return render_template('home.html')
       
@app.route('/display',methods=['GET','POSt'])
def Searching():
    val='a'        
    if request.method=='POST':
        if request.form['submit_button'] == 'All-Data':
            cursor.execute("USE Food")
            cursor.execute("SELECT *FROM food")
            data=cursor.fetchall()
            return render_template('searching.html',val=data)
        else:
            d=dict()
            l=list()
            spincode=int(request.form['spincode'])
            svegetable=str(request.form['svegetable'])
            sfruit=str(request.form['sfruit'])
            cursor.execute("USE Food")
            cursor.execute("SELECT *FROM food")
            for i in cursor.fetchall():
                if (str(i[1])==sfruit) or (str(i[2])== svegetable) or (i[0]==spincode):
                    d['Pincde']=i[0]
                    d['Fruits_Name']=i[1]
                    d['Vegetables_Name']=i[2]
                    l.append(d)      
            return render_template('searching.html',val=l)
        
@app.route('/delete',methods=['GET','POST'])
def delete():
    val="Not Deleted"
    dpi,dfr,dvg=None,None,None
    print(dpi)
    print(dfr)
    print(dvg) 
    if request.method=="POST":
        if request.form['submit_button'] == 'Delete': 
            dpi=int(request.form['dspincode'])
            dfr=str(request.form['dsfruit'])
            dvg=str(request.form['dsvegetable'])
            print(dpi)
            print(dfr)
            print(dvg)
            if dpi != None and dfr=='' and dvg=='':
                cursor.execute("USE Food")
                cursor.execute("DELETE FROM food WHERE Pincode=(%s)",(dpi))
                conn.commit()
                val="Deleted Successful!"
            elif dpi=='' and dfr!=None and dvg=='':
                cursor.execute("USE Food")
                cursor.execute("DELETE FROM food WHERE Fruit_Name=(%s)",(dfr))
                conn.commit()
                val="Deleted Successful!"
            elif dpi=='' and dfr=='' and dvg!=None:
                cursor.execute("USE Food")
                cursor.execute("DELETE FROM food WHERE Vegitable_Name=(%s)",(dvg))
                conn.commit()    
                val="Deleted Successful!"
        else:
            if request.form['submit_button'] == 'All-Data-Delete':
                cursor.execute("USE Food")
                cursor.execute("DELETE FROM food")
                conn.commit()
                val="Deleted All elements Successful!"
    return render_template('deleted.html',value=val)
            

if __name__=='__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)