import random
import names
from random_username.generate import generate_username

# users
cards = ['Chase', 'Apple Card', 'Discover', 'Wells Fargo', 'American Express', 'Citi', 'Bank of America']


# restaurants
restaurants = [
    "BJs",
    "Panda Express", 
    "Tapioca Express", 
    "Cava", 
    "Chipotle", 
    "Nobu Malibu", 
    "The Melt",
    "Curry up Now",
    "Mendocino Farms",
    "ACM Pizza"
]

menu_items = [
    "Cheese Pizza",
    "Boba",
    "Orange Chicken",
    "Mozzarella Sandwich",
    "Falafels",
    "Chicken Burrito",
    "Caviar",
    "Paneer Tikka Masala",
    "Grilled Cheese Sandwich"
]

instructions = [
    "Leave at front door",
    "Ring doorbell",
    "Text me",
    "Leave at back door",
    "Gate code is 1234"
]

statuses = ["Placed", "Cancelled","Delivered"]

create_table_users = "CREATE TABLE users (id SERIAL PRIMARY KEY, first_name VARCHAR(255), last_name VARCHAR(255), username VARCHAR(50), card VARCHAR(255), balance INTEGER);\n"
create_table_orders = "CREATE TABLE courses (id SERIAL PRIMARY KEY, name VARCHAR(255), restaurant VARCHAR(255), quantity INTEGER, instructions VARCHAR(255), cost INTEGER, status VARCHAR(30));\n"
query = ""

# build users insertions
for _ in range(20):
  first_name = names.get_first_name()
  last_name = names.get_last_name()
  username = generate_username(1)
  username = username[0]
  card = random.choice(cards)
  balance = random.randint(0, 1000)

  insert_into_users = "INSERT INTO users (first_name, last_name, username, card, balance) " 
  values = f"VALUES ('{first_name}', '{last_name}', '{username}', '{card}', {balance});\n"

  query += (insert_into_users + values)

query += "\n\n\n"

# build orders insertions
for _ in range(100):
    name = random.choice(menu_items)
    restaurant = random.choice(restaurants)
    quantity = random.randint(0, 6)
    instruction = random.choice(instructions)
    cost = random.randint(0,100)
    status = random.choice(statuses)

    insert_into_orders = "INSERT INTO orders (name, restaurant, quantity, instructions, cost, status) "
    values = f"VALUES ('{name}', '{restaurant}', {quantity}, '{instruction}', {cost}, '{status}');\n"

    query += (insert_into_orders + values)


print(query)