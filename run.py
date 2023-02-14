from flask import jsonify

from app import create_app

data_info = {"character": "/character/information/name", "planet": "/planet/information/name",
             "saga": "/saga/information/name", "fusion": "/fusion/information/name",
             "game": "/videogame/information/name"}

app = create_app()
app.config['JSON_AS_ASCII'] = False


@app.route("/")
def home():
    return jsonify(data_info)


if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
