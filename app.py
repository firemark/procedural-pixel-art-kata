from flask import Flask, redirect, url_for
from datetime import datetime
from procedural_pixel_art.art_generator import PixelArt
import os

app = Flask(__name__)
port = int(os.environ.get("PORT", 5000))


@app.route('/')
def hello_world():
    art = PixelArt()
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    file_name = f"generated_pixel_art_{timestamp}"
    art.save(f"static/{file_name}")
    return '<img src=' + url_for('static', filename=f'{file_name}.png') + '>'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port)
