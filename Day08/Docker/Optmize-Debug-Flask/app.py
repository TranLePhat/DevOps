from flask import Flask
import time

app = Flask(__name__)

@app.route('/')
def hello():
    time.sleep(0.5)  # Giả lập tải nặng
    return "Hello Debug!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)