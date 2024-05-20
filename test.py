from flask import Flask

app = Flask(__name__)

@app.route("/")
def test():
    return "<p>System is Live!</p>"