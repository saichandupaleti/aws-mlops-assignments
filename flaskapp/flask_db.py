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


# Function to insert details
def insert_details(name, data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_with_timestamp = f"{data} (Timestamp: {timestamp})"
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO logs (name, data) VALUES (%s, %s)", (name, data_with_timestamp)
    )
    conn.commit()


# Function to get details
def get_details():
    cur = conn.cursor()
    cur.execute("SELECT name, data FROM logs")
    details = cur.fetchall()
    return details


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form["name"]
        data = request.form["data"]
        insert_details(name, data)
        return redirect(url_for("index"))

    logs = get_details()
    return render_template("index.html", logs=logs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
