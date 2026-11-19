
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! My AWS CI/CD Pipeline is Working Successfully!"

@app.route("/about")
def about():
    return "This is my Python Flask application."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
