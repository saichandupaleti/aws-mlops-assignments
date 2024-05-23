from datetime import datetime

import aws_credentials as rds
import pymysql
from flask import Flask, jsonify, redirect, render_template, request, url_for

app = Flask(__name__)

# Database connection
conn = pymysql.connect(
    host=rds.host,
    port=rds.port,
    user=rds.user,
    password=rds.password,
    db=rds.db,
)


def insert_details(name, data):
    """
    Inserts a log entry into the database with the provided name and data.
    The current timestamp is appended to the data.

    Parameters:
    - name (str): The name associated with the log entry.
    - data (str): The data to be logged.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_with_timestamp = f"{data} (Timestamp: {timestamp})"
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO logs (name, data) VALUES (%s, %s)", (name, data_with_timestamp)
    )
    conn.commit()


def get_details():
    """
    Retrieves all log entries from the database.

    Returns:
    - list of tuples: Each tuple contains the name and data of a log entry.
    """
    cur = conn.cursor()
    cur.execute("SELECT name, data FROM logs")
    details = cur.fetchall()
    return details


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Handles the main page of the application.
    - GET: Displays the form and the list of log entries.
    - POST: Inserts a new log entry and redirects to the main page.

    Returns:
    - str: The rendered HTML of the index page.
    """
    if request.method == "POST":
        name = request.form["name"]
        data = request.form["data"]
        insert_details(name, data)
        return redirect(url_for("index"))

    logs = get_details()
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
