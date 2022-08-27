from flask import Flask
import sqlite3

app = Flask(__name__)


def connect_to_db():
    conn = sqlite3.connect("database.db")
    return conn


def create_db_table():
    try:
        conn = connect_to_db()
        conn.row_factory = sqlite3.Row
        cur = conn.cursor()
        cur.execute("SELECT * FROM games")
        rows = cur.fetchall()
        print(rows)
        if rows is None:
            conn.execute(
                """
        CREATE TABLE games(
        ID INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        company TEXT NOT NULL
        );
      """
            )
            conn.commit()
            print("Table created successfully")
            # Create table
    except:
        print("Table creation failed")
    finally:
        conn.close()


@app.route("/")
def index():
    return "Hello, from Flask!"


@app.route("/all")
def get_all():
    return "Get all data from database"


app.run(host="0.0.0.0", port=81)
