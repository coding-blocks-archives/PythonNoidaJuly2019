from flask import Flask, render_template, request

import product_scrapper

# Engineering Man
# 3 Blue 1 Brown

app = Flask("Comparator")

USERS = [
  {
    "id": 1,
    "name": "Jatin"
  },
  {
    "id": 2,
    "name": "Chirag"
  },
  {
    "id": 3,
    "name": "Kashika"
  },
  {
    "id": 4,
    "name": "Arpit"
  },
]

@app.route('/index')
@app.route('/')
def index():
  return render_template('index.html')

@app.route('/scrapper', methods=['GET', 'POST'])
def scrapper():
  products = []
  if request.method == "POST":
    query = request.form["query"]
    products = product_scrapper.scrap(query)
  return render_template('scrapper.html', products = products)

@app.route('/users')
def users():
  return render_template('users.html', users = USERS)

@app.route('/users/<int:id>')
def user(id):
  for user in USERS:
    if user["id"] == id:
      return render_template('user.html', user = user)
  return "Not Found :'("

app.run(port = 8000, debug = True)
