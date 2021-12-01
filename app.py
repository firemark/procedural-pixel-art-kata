from flask import Flask, redirect, url_for, render_template
from flask import send_file
from datetime import datetime
from procedural_pixel_art.art_generator import PixelArt

from tempfile import NamedTemporaryFile
from shutil import copyfileobj
from os import remove
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


@app.route('/image.png')
def get_image():
	file_name = "myfile"
	file_path = f"static/{file_name}"
	art = PixelArt()
	art.save(file_path)
	response = send_file(f"{file_path}.png", mimetype='image/png')
	return response


@app.route('/andrzejki')
def andrzejki():
	return render_template("andrzejki.html")


if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=port)
