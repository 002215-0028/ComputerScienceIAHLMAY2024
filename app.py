import os
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from help import employee, customer, Node, Stack, generate_unique_order_id, login_required, count_digits
import string    
import random 
import datetime
import sys
from random import randint
path = '/home/yourusername/mysite'
if path not in sys.path:
   sys.path.insert(0, path)

#from flask_app import app as application

app = Flask(__name__)
app.config["TEMPLATES_AUTO_RELOAD"] = True
db = SQL("sqlite:///data/ia.db")
currentDateTime = datetime.datetime.now()

@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/indexproduction", methods=["GET", "POST"])
#opens when the production employee logs in to read updates on the production
#helps plan resources and time for the impending stages
def indexproduction():
    #check session
    user_id = session["user_id"]
    order_id = session["order_id"]
    #select data from production table
    production = db.execute("SELECT * FROM production WHERE production_id IN (SELECT order_id FROM orders WHERE completed = 0);")
    if request.method == "POST":
        if (not request.form.get("field")) or (not request.form.get("data")) :
            return render_template ("update.html")
        else:
            field = request.form.get("field")
            data = request.form.get("data")
             #use data from form to check what the employee wants to update and take teh data value to make it the new value of that attribute
            if field == 'paddy_quality':
                a = db.execute("UPDATE production SET paddy_quality = ? WHERE production_id = ?;", data, order_id)
            if field == 'paddy_quantity':
                a = db.execute("UPDATE production SET paddy_quantity = ? WHERE production_id = ?;", data, order_id)
            if field == 'paddy_rate':
                a = db.execute("UPDATE production SET paddy_rate = ? WHERE production_id = ?;", data, order_id)
            if field == 'paddy_ordered':
                a = db.execute("UPDATE production SET paddy_ordered = ? WHERE production_id = ?;", data, order_id)
            if field == 'paddy_stored':
                a = db.execute("UPDATE production SET paddy_stored = ? WHERE production_id = ?;", data, order_id)
            if field == 'cleaning':
                a = db.execute("UPDATE production SET cleaning = ? WHERE production_id = ?;", data, order_id)
            if field == 'removal_of_husk':
                a = db.execute("UPDATE production SET removal_of_husk = ? WHERE production_id = ?;", data, order_id)
            if field == 'paddy_separation':
                a = db.execute("UPDATE production SET paddy_separation = ? WHERE production_id = ?;", data, order_id)
            if field == 'polishing':
                a = db.execute("UPDATE production SET polishing = ? WHERE production_id = ?;", data, order_id)
            if field == 'parboiling':
                a = db.execute("UPDATE production SET parboiling = ? WHERE production_id = ?;", data, order_id)
            if field == 'drying':
                a = db.execute("UPDATE production SET drying = ? WHERE production_id = ?;", data, order_id)
            if field == 'packaging':
                a = db.execute("UPDATE production SET packaging = ? WHERE production_id = ?;", data, order_id)
            time = db.execute("UPDATE production SET updated_at = ?", currentDateTime)
            production = db.execute("SELECT * FROM production WHERE production_id = ?;", order_id)
            return render_template("indexproduction.html", production = production) 


@app.route("/indexshipment", methods=["GET", "POST"])
def indexshipment():
    #check session
    user_id = session["user_id"]
    order_id = session["order_id"]
    #select data from shipments table
    shipment = db.execute("SELECT * FROM shipment WHERE shipment_id = ?;", order_id)
    if request.method == "POST":
        if (not request.form.get("field")) or (not request.form.get("data")) :
            return render_template ("update.html")
        else:
            field = request.form.get("field")
            data = request.form.get("data")
             #use data from form to check what the employee wants to update and take teh data value to make it the new value of that attribute
            if field == 'shipment_company':
                a = db.execute("UPDATE shipment SET shipment_company = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'shipment_location':
                a = db.execute("UPDATE shipment SET shipment_location = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'shipment_number':
                a = db.execute("UPDATE shipment SET shipment_numberTEXT = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'truck_reached':
                a = db.execute("UPDATE shipment SET truck_reached = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'truck_loaded':
                a = db.execute("UPDATE shipment SET truck_loaded = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'truck_left':
                a = db.execute("UPDATE shipment SET truck_left = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'reached_container':
                a = db.execute("UPDATE shipment SET reached_container = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'container_loaded':
                a = db.execute("UPDATE shipment SET container_loaded = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'container_left':
                a = db.execute("UPDATE shipment SET container_left = ? WHERE shipment_id = ?;", data, order_id)
            if field == 'delivered':
                a = db.execute("UPDATE shipment SET delivered = ? WHERE shipment_id = ?;", data, order_id)
            time = db.execute("UPDATE shipment SET updated_at = ?", currentDateTime)
            shipment = db.execute("SELECT * FROM shipment WHERE shipment_id = ?;", order_id)
            return render_template("indexshipment.html", shipment = shipment) 


@app.route("/indexfinance", methods=["GET", "POST"])
def indexfinance():
    #check session
    user_id = session["user_id"]
    order_id = session["order_id"]
    #select data from finances table
    finances = db.execute("SELECT * FROM finance WHERE finance_id IN (SELECT order_id FROM orders WHERE completed = 0);")
    if request.method == "POST":
        if (not request.form.get("field")) or (not request.form.get("data")) :
            return render_template ("update.html")
        else:
            field = request.form.get("field")
            data = request.form.get("data")
            #use data from form to check what the employee wants to update and take teh data value to make it the new value of that attribute
            if field == 'docs_in_bank':
                a = db.execute("UPDATE finance SET docs_in_bank = ? WHERE finance_id = ?;", data, order_id)
            if field == 'docs_submitted':
                a = db.execute("UPDATE finance SET docs_submitted = ? WHERE finance_id = ?;", data, order_id)
            if field == 'request_payment':
                a = db.execute("UPDATE finance SET request_payment = ? WHERE finance_id = ?;", data, order_id)
            if field == 'payment_received':
                a = db.execute("UPDATE finance SET payment_received = ? WHERE finance_id = ?;", data, order_id)
            time = db.execute("UPDATE finance SET updated_at = ?", currentDateTime)
            finances = db.execute("SELECT * FROM finance WHERE finance_id = ?;", order_id)

            return render_template("indexfinance.html", finances = finances) 


@app.route("/customerhomepage", methods=["GET", "POST"])
def customerhomepage():
    if request.method == "POST":
        if not request.form.get("choice"):
            return render_template("customerhomepage.html")
        choice = request.form.get("choice")
        #uses data from form to allow the customer to access different functionalities of the system 
        if choice == 'update':
            return redirect("/update")
        if choice == 'payment':
            return redirect("/payment")
        if choice == 'contactteam':
            return redirect("/contactteam")
    else:
        return render_template("customerhomepage.html")

@app.route("/update", methods=["GET", "POST"])
@login_required
def update():
    #saves session of user
    user_id = session["user_id"]
    if request.method == "POST":
        if not request.form.get("order_id"):
        #checks order_id has been inputted
            return render_template ("update.html")
        else:
            order_id = request.form.get("order_id")
            #select data from the table with that order_id
            rows = db.execute("SELECT * FROM orders WHERE order_id = ?", order_id)
            if len(rows) != 1:
              return render_template("update.html")
        #create a session with tha order_id
        session["order_id"] = rows[0]["order_id"]
        order = db.execute("SELECT * FROM orders WHERE order_id = ?", order_id)
        production = db.execute("SELECT * FROM production WHERE production_id = ?;", order_id)
        shipment = db.execute("SELECT * FROM shipment WHERE shipment_id =?;", order_id)
        finances = db.execute("SELECT * FROM finance WHERE finance_id = ?;", order_id)
        #if user is employee
        if count_digits(user_id) == 3:
            #if user is production employee
            if int(user_id)%3 == 0:
                return render_template("indexproduction.html", production = production, order=order)
            #if user is shipment employee
            if int(user_id)%3 == 1:   
                return render_template("indexshipment.html", shipment = shipment, order=order)
            #if user is finance employee
            if int(user_id)%3 == 2:  
                return render_template("indexfinance.html", finances = finances, order=order) 
        #if user is administrator
        if count_digits(user_id) == 2:
            return redirect("/orderdetails")
        #if user is customer
        if count_digits(user_id) == 4:
            return render_template("indexcustomer.html", order = order, production = production, shipment = shipment, finances = finances)
    else:
        return render_template ("update.html")


@app.route("/payment", methods=["GET", "POST"])
def payment():
    #if customer does payment
    order_id = request.form.get("order_id")   
    if request.method == "POST":
        #update finances table and mark order as complete automatically
        f = db.execute("UPDATE finance SET payment_received = ? WHERE finance_id = ?;", "yes", order_id)
        o = db.execute("UPDATE orders SET completed = ? WHERE order_id = ?;", "yes", order_id)
        return redirect("/customerhomepage")
    else:
        return render_template ("payment.html")


@app.route("/contactteam", methods=["GET", "POST"])
def contactteam():
    #all displayed on the HTML file itself
    return render_template ("contactteam.html")

@app.route("/administratorhomepage", methods=["GET", "POST"])
def administratorhomepage():
    if request.method == "POST":
        if not request.form.get("option"):
            return render_template("administratorhomepage.html")
        option = request.form.get("option")
        #uses the form to redirect the administrator to different pages to access different functionalities of the system 
        if option == 'orderdetails':
            return redirect("/update")
        if option == 'employeedetails':
            return redirect("/employeedetails")
        if option == 'neworder':
            return redirect("/neworder")
        if option == 'completeorder':
            return redirect("/completeorder")
        if option == 'orderhistory':
            return redirect("/orderhistory")
    else:
        return render_template("administratorhomepage.html")

@app.route("/completeorder", methods=["GET", "POST"])
def completeorder():
    #check what kind of user it is 
    user_id = session["user_id"]
    orders = db.execute("SELECT * FROM orders ;")
    if request.method == "POST":
        if not request.form.get("order_id"):
            return render_template("completeorder.html")
        else:
            order_id = request.form.get("order_id")
            a = db.execute("SELECT completed FROM orders WHERE order_id = ?", order_id)
            if len(a) == 1:
                x = db.execute("SELECT payment_received FROM finance WHERE finance_id = ?", order_id)
                #check if payment of that order has been done
                if x == "yes":
                    #if yes, mark it complete
                    b = db.execute("UPDATE orders SET completed = ? WHERE order_id = ?", "yes", order_id)
                    user_name = db.execute("SELECT user_name FROM users WHERE user_id = ?", order_id)
                    description = db.execute("SELECT description FROM users WHERE user_id = ?", order_id)
                    password = db.execute("SELECT password FROM users WHERE user_id = ?", order_id)
                    #identify customer object and remove it from the database
                    cust = customer(user_id, user_name, description, password)
                    cust.remove()
            return redirect("/administratorhomepage")
    else:
        return render_template ("completeorder.html")

@app.route("/orderdetails", methods=["GET", "POST"])
def orderdetails():
    #check order session
    order_id = session["order_id"]
    data = request.form.get("data")
    #select data from the orders' tables
    orders = db.execute("SELECT * FROM orders WHERE order_id = ?", order_id)
    production = db.execute("SELECT * FROM production WHERE production_id = ?", order_id)
    shipment = db.execute("SELECT * FROM shipment WHERE shipment_id = ?", order_id)
    finance = db.execute("SELECT * FROM finance WHERE finance_id = ?", order_id)
    #take feedbck from administrator
    if request.method == "POST":
        a = db.execute("UPDATE orders SET feedback_from_administrator = ? WHERE order_id = ?;", data, order_id)
    time = db.execute("UPDATE orders SET updated_at = ?", currentDateTime)
    orders = db.execute("SELECT * FROM orders WHERE order_id = ?", order_id)
    return render_template ("orderdetails.html", orders = orders, production = production, shipment = shipment, finance = finance)


@app.route("/indexcustomer", methods=["GET", "POST"])
def indexcustomer():
    #check the session
    order_id = session["order_id"]
    data = request.form.get("data")
    #select data from the tables
    order = db.execute("SELECT * FROM orders WHERE order_id = ?", order_id)
    production = db.execute("SELECT * FROM production WHERE production_id = ?", order_id)
    shipment = db.execute("SELECT * FROM shipment WHERE shipment_id = ?", order_id)
    finance = db.execute("SELECT * FROM finance WHERE finance_id = ?", order_id)
    #take feedback from the customer
    if request.method == "POST":
        a = db.execute("UPDATE orders SET feedback_from_customer = ? WHERE order_id = ?;", data, order_id)
    time = db.execute("UPDATE orders SET updated_at = ?", currentDateTime)
    order = db.execute("SELECT * FROM orders WHERE order_id = ?", order_id)
    return render_template ("indexcustomer.html", order = order, production = production, shipment = shipment, finance = finance)

@app.route("/neworder", methods=["GET", "POST"])
def neworder():
    if request.method == "POST":
        if not request.form.get("order_name"):
        #if no input, display error message
            return render_template("neworder.html", message = 'Please enter order_name')
        elif not request.form.get("predicted_time"):
            return render_template("neworder.html", message = 'Please enter predicted time for completion')
        #save values in variables
        predicted_time = request.form.get("predicted_time")
        order_name = request.form.get("order_name")
        orderids = db.execute('SELECT order_id FROM orders;')
        #call function from help.py which makes unique order_ids
        order_id = generate_unique_order_id(orderids)
        #insert them into the respective tables
        o = db.execute("INSERT INTO orders(order_id, order_name, predicted_time) VALUES(?,?,?)", order_id, order_name, predicted_time)
        p = db.execute("INSERT INTO production(production_id) VALUES(?);", order_id)
        s = db.execute("INSERT INTO shipment(shipment_id) VALUES(?);", order_id)
        f = db.execute("INSERT INTO finance(finance_id) VALUES(?);", order_id)
        #create a customer object
        s = 16
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))    
        password = str(ran)
        description = "customer"
        cust = customer(order_id, order_name, description, password)
        #add the customer to the users database by the method save()
        cust.save()
        return render_template("update.html", message = (" new order_id: ", order_id))
    return render_template ("neworder.html")

@app.route("/orderhistory", methods=["GET", "POST"])
def orderhistory():
    #select all completed orders
    orders = db.execute("SELECT * FROM orders WHERE completed = ?; ", 'yes')
    # select all order_ids of completed orders
    orderids = db.execute("SELECT order_id FROM orders WHERE completed = ?;", 'yes')
    #put them all into a stack by using the method push()
    #for i in range(len(orderids)):
        #idslist = Stack()
        #idslist.push(orderids[i]['order_id'])
    #select the respective detaisl from production,shipment, finance
    production = db.execute("SELECT * FROM production WHERE production_id IN (SELECT order_id FROM orders WHERE completed ='yes' );")
    shipment = db.execute("SELECT * FROM shipment WHERE shipment_id IN (SELECT order_id FROM orders WHERE completed = 'yes'); ")
    finance = db.execute("SELECT * FROM finance WHERE finance_id IN (SELECT order_id FROM orders WHERE completed = 'yes'); ")
    #display on HTML file
    return render_template ("orderhistory.html", orders = orders, production = production, shipment = shipment, finance = finance)

@app.route("/employeedetails", methods=["GET", "POST"])
def employeedetails():
    #selects user details from the database and displays it in the HTML file
    users = db.execute('SELECT * FROM users WHERE description = ? OR description = ? OR description = ?;', 'production', 'finance', 'shipment')
    return render_template ("employeedetails.html", users = users)

@app.route("/generateemployee", methods=["GET", "POST"])
def generateemployee():
    #checks if method is post
    if request.method == "POST":
        if not request.form.get("user_name"):
            #displays error message if no input
            return render_template("generateemployee.html", message = 'Please enter user_name')
        elif not request.form.get("description"):
            #displays error message if no input
            return render_template("login.html", message = 'Please enter description of user')
        #save values in variables
        user_name = request.form.get("user_name")
        description = request.form.get("description")
        users = db.execute('SELECT * FROM users;')
        userids = db.execute('SELECT user_id FROM users;')
        #generate a random 3 digit user_id 
        user_id = randint(100, 999)
        if user_id in userids:
            # if it already exists in the database then change it
            user_id +=1
        #create a random complex string password
        s = 16
        ran = ''.join(random.choices(string.ascii_uppercase + string.digits, k = s))    
        password = str(ran)
        #create an employee object
        emp = employee(user_id, user_name, description, password)
        #add the object to the database by calling the method save()
        emp.save()
        return redirect("/employeedetails")
    else:
        return render_template ("generateemployee.html")

@app.route("/removeemployee", methods=["GET", "POST"])
def removeemployee():
    #checks if method is post
    if request.method == "POST":
    #if there is no input for user_id, displays error message
        if not request.form.get("user_id"):
            return render_template("removeemployee.html", message = 'Please enter user_id')
        #save the results in a variable
        user_id = request.form.get("user_id")
        user_name = db.execute("SELECT user_name FROM users WHERE user_id = ?;", user_id)
        description = db.execute("SELECT description FROM users WHERE user_id = ?;", user_id)
        password = db.execute("SELECT password FROM users WHERE user_id = ?;", user_id)
        #create employee object
        emp = employee(user_id, user_name, description, password)
        #call the method to remove the employee from the database
        emp.remove()
        return redirect("/employeedetails")
    else:
        return render_template ("removeemployee.html")

@app.route("/", methods=["GET", "POST"])
def login():
    #reset the session
    session.clear()
    message = 'Hello!'
    if request.method == "POST":
        #check if user_id is inputted 
        if not request.form.get("user_id"):
            return render_template("login.html", message = 'Please enter user_id')
        elif not request.form.get("password"):
            #check if password is inputted
            return render_template("login.html", message = 'Please enter password')
        #find the user in the table 'users'
        user_id = request.form.get("user_id")
        rows = db.execute("SELECT * FROM users WHERE user_id = ?", user_id)
        if len(rows) != 1:
            #if it does not exist, ask them to log in again
            return render_template("login.html", message = 'Please enter valid user_id/password')
        #start a new session for the user
        session["user_id"] = rows[0]["user_id"]
        if not request.form.get("user"):
            #checks if type of user is filled
            return render_template("index.html", message = 'Please choose an option')
        #the following is the authorisation process
        user = request.form.get("user")
        orders = db.execute("SELECT * FROM orders;")
        if user == 'employee':
            #if user inputs employee, it checks if the user_id is valid for an employee(Should be three digits)
            if count_digits(request.form.get("user_id")) == 3:
                    return render_template ("update.html")
            else:
                return render_template ("login.html", message = 'Authorisation failed') 
        if user == 'administrator':
            #if user inputs administrator, it checks if the user_id is valid(should be two digits only)
            if count_digits(request.form.get("user_id")) == 2: 
                return render_template ("administratorhomepage.html", orders = orders)
            else: 
                return render_template ("login.html", message = 'Authorisation failed') 
        if user == 'customer':
            #if user inputs administrator, it checks if the user_id is valid(should be four digits only)
            if count_digits(request.form.get("user_id")) == 4:
                return render_template ("customerhomepage.html", orders = orders)
            else: 
                return render_template ("login.html", message = 'Authorisation failed') 
    else:
        return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    return redirect("/")