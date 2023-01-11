# Install
# pip install Flask

# Run
# flask --app P143_flask run

from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Hello, Flask!</p>"
