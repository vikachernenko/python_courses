from flask import Flask
from src import api_manipulator

app = Flask(__name__, static_url_path="", static_folder="public")


@app.route("/api/generate", methods=["POST"])
def generate_api():
    api_manipulator.generate_api()
    return api_manipulator.get_api()


@app.route("/")
def get_api():
    return api_manipulator.get_api()


if __name__ == '__main__':
    api_manipulator.generate_api()  # Генерация при запуске сервера
    app.run(host="0.0.0.0", port=80, debug=True)
