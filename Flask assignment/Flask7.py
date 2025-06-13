#7. Integrate a SQLite database with Flask to perform CRUD operations on a list of items.
from flask import Flask, render_template, request, redirect
import sqlite3
import os

app = Flask(__name__)
if not os.path.exists("database"):
    os.makedirs("database")

def create():
    con = sqlite3.connect("database/newdatabase.db")
    cur = con.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS items (id INTEGER PRIMARY KEY, name TEXT, age INTEGER, city TEXT)")
    con.commit()
    con.close()
create()

@app.route("/")
def home():
    edit_id = request.args.get("edit_id", type=int)
    con = sqlite3.connect("database/newdatabase.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM items")
    items = cur.fetchall()
    con.close()
    return render_template("items_list.html", items=items, edit_id=edit_id)

@app.route("/add", methods=["POST"]) 
def add():
    name = request.form["name"]
    age = request.form["age"]
    city = request.form["city"]
    con = sqlite3.connect("database/newdatabase.db")
    cur = con.cursor()
    cur.execute("INSERT INTO items (name, age, city) VALUES (?, ?, ?)", (name, age, city))  
    con.commit()
    con.close()
    return redirect("/")

@app.route("/delete/<int:item_id>")
def delete(item_id):
    con = sqlite3.connect("database/newdatabase.db")
    cur = con.cursor()
    cur.execute("DELETE FROM items WHERE id = ?", (item_id,)) 
    con.commit()
    con.close()
    return redirect("/")

@app.route("/update/<int:item_id>", methods=["POST"])
def update(item_id):
    name = request.form["name"]
    age = request.form["age"]
    city = request.form["city"]
    con = sqlite3.connect("database/newdatabase.db")
    cur = con.cursor()
    cur.execute("UPDATE items SET name=?, age=?, city=? WHERE id=?", (name, age, city, item_id))
    con.commit()
    con.close()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)