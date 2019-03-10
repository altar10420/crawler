from flask import Flask, render_template, request
import backend
from backend_database import Database
from sqlite3 import IntegrityError


app = Flask(__name__)


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
        database = Database("users.db")
        try:
            database.insert(email, top_price)
        except IntegrityError:
            print("Database error while entering data.")
            return render_template("error.html")

    return render_template("subscribe.html")


@app.route('/unsubscribe', methods=['POST'])
def unsubscribe():

    if request.method == 'POST':
        email = request.form["email_name"]
        database = Database("users.db")
        try:
            database.delete(email)
        except IntegrityError:
            print("Database error while deleting data.")
            return render_template("error.html")

    return render_template("unsubscribe.html")


if __name__ == "__main__":
    app.run(debug=True)
