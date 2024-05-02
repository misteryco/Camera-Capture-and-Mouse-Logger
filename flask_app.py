import os
from io import BytesIO

from flask import Flask, render_template, request, send_file
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker

from models import CapturedImageModel

app = Flask(__name__)

db_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), "captured_images.db")
app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{db_path}"
db = SQLAlchemy(app)


@app.route('/data', methods=['GET'])
def read_from_database():
    if request.method == 'GET':
        session = sessionmaker(bind=db.engine)()
        rows = session.query(CapturedImageModel).all()
        return render_template('data.html', rows=rows)
    return "Method Not Allowed", 405


@app.route('/download_image/<int:image_id>')
def download_image(image_id):
    session = sessionmaker(bind=db.engine)()
    image_entry = session.query(CapturedImageModel).get(image_id)

    if image_entry is None or image_entry.image_source is None:
        return "Image not found", 404

    # BytesIO object
    image_data = BytesIO(image_entry.image_source)

    return send_file(
        image_data,
        mimetype='image/png',
        as_attachment=True,
        download_name=f'{image_entry.path}'
    )


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run()
