from flask import Flask, request, jsonify
import pymysql
import os

app = Flask(__name__)

# Database connection parameters
db_host = os.getenv("MYSQL_HOST", "localhost")
db_user = os.getenv("MYSQL_USER", "root")
db_password = os.getenv("MYSQL_PASSWORD", "")
db_name = os.getenv("MYSQL_DB", "testdb")

def get_connection():
    return pymysql.connect(
        host=db_host,
        user=db_user,
        password=db_password,
        database=db_name,
        cursorclass=pymysql.cursors.DictCursor,
    )

# Create table if not exists
with get_connection() as conn:
    with conn.cursor() as cursor:
        cursor.execute(
            """CREATE TABLE IF NOT EXISTS items (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255) NOT NULL
            )"""
        )
    conn.commit()

@app.route("/")
def index():
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("SELECT * FROM items")
            items = cursor.fetchall()
    return jsonify(items)

@app.route("/item", methods=["POST"])
def create_item():
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO items (name) VALUES (%s)", (name,))
        conn.commit()
    return jsonify({"message": "Item created"}), 201

@app.route("/item/<int:item_id>", methods=["PUT"])
def update_item(item_id):
    data = request.json
    name = data.get("name")
    if not name:
        return jsonify({"error": "Name is required"}), 400
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("UPDATE items SET name=%s WHERE id=%s", (name, item_id))
        conn.commit()
    return jsonify({"message": "Item updated"})

@app.route("/item/<int:item_id>", methods=["DELETE"])
def delete_item(item_id):
    with get_connection() as conn:
        with conn.cursor() as cursor:
            cursor.execute("DELETE FROM items WHERE id=%s", (item_id,))
        conn.commit()
    return jsonify({"message": "Item deleted"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

