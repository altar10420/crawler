from flask import Flask, render_template, request
import backend
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

# use locally
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/crawler'


db = SQLAlchemy(app)


class Data(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    email_ = db.Column(db.String(120), unique=True)
    price_ = db.Column(db.Integer)

    def __init__(self, email_, price_):
        self.email_ = email_
        self.price_ = price_

    def __repr__(self):
        return '<User {}>'.format(self.email_)


# now in python console crete database columns
# python3
# from app import db
# db.create_all()


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/subscribe', methods=['POST'])
def subscribe():
    # return render_template("check_now.html")

    if request.method == 'POST':
        email = request.form["email_name"]
        top_price = request.form["top_price_name"]
        backend.flat_spider(email, top_price)
        try:
            data = Data(email, top_price)
            db.session.add(data)
            db.session.commit()
        except:
            print("Database error while deleting data.")
            return render_template("error.html")

    return render_template("subscribe.html")


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():

    if request.method == 'POST':
        email = request.form["email_name"]
        data = Data.query.filter_by(email_=email)
        data.delete()
        db.session.commit()

    return render_template("unsubscribe.html")


if __name__ == "__main__":
    app.run(debug=True)
