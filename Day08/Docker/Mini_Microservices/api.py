from flask import Flask
import psycopg2

app = Flask(__name__)

@app.route('/users')
def get_users():
    conn = psycopg2.connect("dbname=users user=postgres password=mysecret host=db")
    cur = conn.cursor()
    cur.execute("SELECT * FROM users;")
    data = cur.fetchall()
    conn.close()
    return str(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)