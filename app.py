from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://postgres:password@localhost/data_collector'
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
        bday = request.form["birthday_field"]
    print(email,bday)
    return render_template("success.html")

if __name__ == "__main__":
    app.debug=True
    app.run()