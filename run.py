from flask import jsonify
from app import create_app

app = create_app()
app.config['JSON_AS_ASCII'] = False

if __name__ == "__main__":
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
