from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_email import send_email
from datetime import datetime

app = Flask(__name__)
# app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/data_collector'
# URI for Heroku db
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgres://hxukgirxrvwjzh:ec3f3035fcf5dc6cbde92a41c537efd0319ec8c14a744ade91625b5db252773a@ec2-54-165-36-134.compute-1.amazonaws.com:5432/d9p8ahkm69hbbs?sslmode=require'
db = SQLAlchemy(app)

class Data(db.Model):
    __tablename__ = "data"
    id = db.Column(db.Integer, primary_key=True)
    email_= db.Column(db.String(120), unique=True)
    bday_ = db.Column(db.Date)

    def __init__(self,email_,bday_):
        self.email_=email_
        self.bday_=bday_

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/success", methods = ['POST'])
def success():
    if request.method=='POST':
        email= request.form["email_field"]
        bday =  datetime.strptime(request.form["birthday_field"], "%Y-%m-%d").date()
        date_diff = datetime.now().date() - bday
        age = date_diff.days
        send_email(email,bday,age)
    if db.session.query(Data).filter(Data.email_==email).count() == 0:
        input_data = Data(email,bday)
        db.session.add(input_data)
        db.session.commit()
        return render_template("success.html")
    return render_template("index.html" , text = "The Email id you have provided already exists in our database!")

if __name__ == "__main__":
    app.debug=True
    app.run()