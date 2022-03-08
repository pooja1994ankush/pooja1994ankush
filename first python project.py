from flask import *
import pymysql as pm

db=pm.connect(host="localhost",user="root",password="",database="shop")

cursor=db.cursor()

app=Flask(__name__)

@app.route("/")
def hello_world():
    return render_template("home1.html")

@app.route("/formale")
def formale():
    q="SELECT * FROM male"
    cursor.execute(q)
    result=cursor.fetchall()

    return render_template("male.html",data=result)

@app.route("/addp",methods=["POST"] )
def addp():
    product_name=request.form['pname']
    product_details=request.form['pdetails']
    price=request.form['price']
    available_quantity=request.form['quantity']
    qr="INSERT INTO male(product_name,product_details,price,available_quantity) VALUES('{}','{}','{}','{}')".format(product_name,product_details,price,available_quantity)
    try:
        cursor.execute(qr)
        db.commit()
        return redirect(url_for("formale"))
    except:
        db.rollback()
        return "Error in query"
    
@app.route("/delete")
def deletep ():
    id=request.args['id']
    delq="DELETE FROM male WHERE id={}".format(id)
    try:
        cursor.execute(delq)
        db.commit()
        return redirect(url_for("formale"))
    except:
        db.rollback()
        return "Error in query"

@app.route ("/edit")
def editp():
    id=request.args['id']
    singleqr="SELECT * FROM male WHERE id='{}'".format(id)
    cursor.execute(singleqr)
    singleres=cursor.fetchone()
    
    return render_template("editp.html",singuser=singleres)

@app.route ("/buyp")
def buyp():
    id=request.args['id']
    singleqr="SELECT * FROM male WHERE id='{}'".format(id)
    cursor.execute(singleqr)
    res=cursor.fetchone()
    
    return render_template("buy.html",singuser=res)

@app.route("/buyed")
def buyed():
    return render_template("buyed.html")

@app.route("/updatep",methods=["POST"])
def updatep():
    product_name=request.form['pname']
    product_details=request.form['pdetails']
    price=request.form['price']
    available_quantity=request.form['quantity']
    pid=request.form['pid']
    
    upq="UPDATE male SET product_name='{}',product_details='{}',price='{}',available_quantity='{}'  WHERE id='{}' ".format(product_name,product_details,price,available_quantity,pid)
    
    
    try:
        cursor.execute(upq)
        db.commit()
        return redirect(url_for("formale"))
    except:
        db.rollback()
        return "Error in query"    

@app.route("/forfemale")
def forfemale():
    q="SELECT * FROM female"
    cursor.execute(q)
    result=cursor.fetchall()

    return render_template("female.html",data=result)
   

@app.route("/addpf",methods=["POST"] )
def addpf():
    product_name=request.form['pname']
    product_details=request.form['pdetails']
    price=request.form['price']
    available_quantity=request.form['quantity']
    qr="INSERT INTO female(product_name,product_details,price,available_quantity) VALUES('{}','{}','{}','{}')".format(product_name,product_details,price,available_quantity)

    try:
        cursor.execute(qr)
        db.commit()
        return redirect(url_for("forfemale"))
    except:
        db.rollback()
        return "Error in query"    

@app.route("/delete")
def deletepf ():
    id=request.args['id']
    delqr="DELETE FROM female WHERE id={}".format(id)
    try:
        cursor.execute(delqr)
        db.commit()
        return redirect(url_for("forfemale"))
    except:
        db.rollback()
        return "Error in query"

@app.route ("/editpf")
def editpf():
    id=request.args['id']
    singleqr1="SELECT * FROM female WHERE id='{}'".format(id)
    cursor.execute(singleqr1)
    singleres=cursor.fetchone()
    
    return render_template("editpf.html",singuser=singleres)

@app.route("/updatepf",methods=["POST"])
def updatepf():
    product_name=request.form['pname']
    product_details=request.form['pdetails']
    price=request.form['price']
    available_quantity=request.form['quantity']
    pid=request.form['pid']
    
    upqr="UPDATE female SET product_name='{}',product_details='{}',price='{}',available_quantity='{}'  WHERE id='{}' ".format(product_name,product_details,price,available_quantity,pid)
    
    
    try:
        cursor.execute(upqr)
        db.commit()
        return redirect(url_for("forfemale"))
    except:
        db.rollback()
        return "Error in query" 

@app.route ("/buypf")
def buypf():
    id=request.args['id']
    singleqr1="SELECT * FROM female WHERE id='{}'".format(id)
    cursor.execute(singleqr1)
    res=cursor.fetchone()
    
    return render_template("buy1.html",singuser=res)    

@app.route("/buyedf")
def buyedf():
    return render_template("buyed.html")
    
if __name__=="__main__":
    app.run(debug=True)    

