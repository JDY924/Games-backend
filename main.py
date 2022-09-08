from flask import (
    Flask,  # for creating a flask app
    request,  # for receiving data
    jsonify,  # for sending data as json
)
import sqlite3  # for the database


# db setup
db = sqlite3.connect("database.db")
cursor = db.cursor()
cursor.execute(
    """
        CREATE TABLE games(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        company TEXT NOT NULL
        );
      """
)
db.commit()
# /db setup

app = Flask(__name__)


def sql(cmd, vals=None):
    conn = sqlite3.connect("database.db")
    cur = conn.cursor()
    res = cur.execute(cmd, vals).fetchall()
    conn.commit()
    conn.close()
    return res


@app.route("/")
def index():
    return "Hello, from Flask!"


@app.route("/all", methods=["GET"])
def all():
    try:
        response = sql("SELECT * FROM games")
        response = jsonify(response)
        if response is None:
            return "NOthing in DB"
        return response
    except:
        print("Connection to DB failed")
        return "Connection to DB failed"


@app.route("/place", methods=["POST"])
def place():
    response = sql(
        "INSERT INTO games (name, company) VALUES (?, ?)",
        (request.form["name"], request.form["company"]),
    )
    return response


app.run(host="0.0.0.0", port=81)
