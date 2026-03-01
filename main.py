from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Hello, World, Bach!"


if __name__ == "__main__":
    # Run the app on a local server, debug=True provides helpful error pages
    app.run(port=5000)
