import backend
from backend_database import Database


database = Database("users.db")

# print(database.view()[0][1])
#
# email = database.view()[0][1]
# price = database.view()[0][2]

for row in database.view():
    # print(row)
    email = row[1]
    price = row[2]
    print(email + " " + str(price))
    backend.flat_spider(email, price)

