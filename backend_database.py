# import sqlite3
from flask_sqlalchemy import SQLAlchemy


# class Database:
#
#     def __init__(self, db):
#         self.conn = sqlite3.connect(db)
#         self.cur = self.conn.cursor()
#         self.cur.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, email text UNIQUE, price INTEGER)")
#         self.conn.commit()
#
#     def insert(self, email, price):
#         self.cur.execute("INSERT OR IGNORE INTO users VALUES (NULL, ?, ?)", (email, price))  # if row exists ignore
#         self.cur.execute("UPDATE users SET price=(?)", (price,))  # comma at the end if we want to pass a tuple
#         self.conn.commit()
#
#     def view(self):
#         self.cur.execute("SELECT * FROM users")
#         rows = self.cur.fetchall()
#         return rows
#
#     def delete(self, email):
#         self.cur.execute("DELETE FROM users WHERE email=(?)", (email,))  # no comma at the end if only single variable passed
#         self.conn.commit()

# app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/cralwer'
# db=SQLAlchemy(app)

#class Database()
