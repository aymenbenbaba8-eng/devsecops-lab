

from flask import Flask, request
import sqlite3

app = Flask(__name__)


@app.route("/login", methods=["POST"])
def login():
    username = request.json.get("username")
    password = request.json.get("password")

    if not username or not password:
        return {"error": "Missing credentials"}, 400

    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    
    query = "SELECT * FROM users WHERE username = ? AND password = ?"
    cursor.execute(query, (username, password))

    result = cursor.fetchone()
    conn.close()

    if result:
        return {"status": "success", "user": username}

    return {"status": "error", "message": "Invalid credentials"}, 401


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
