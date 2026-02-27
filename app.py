from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "Bankai"


if __name__ == "__main__":
    print("WEB SERBER IS RUNNING \n\n\n\n\n\n\nserver workinggggggggggggggg")
    app.run()
