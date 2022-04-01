from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "Welcome to machine learning model APIs!"


if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host='0.0.0.0', debug=True)