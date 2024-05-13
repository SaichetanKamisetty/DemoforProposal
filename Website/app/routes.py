from flask import render_template, request
from app import app
import os
import sys
sys.path.insert(1, 'Website/app/static/')
import controller
from werkzeug.utils import secure_filename

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/uploadWebtoon', methods=['POST'])
def validate_and_modify():
    uploaded_files = request.files.getlist('files[]')

    if not os.path.exists('Website/app/static/uploads'):
        os.makedirs('Website/app/static/uploads')

    filenames = []
    for file in uploaded_files:
        filename = secure_filename(file.filename)
        file_path = os.path.join('Website/app/static/uploads', filename)
        file_path_fix = os.path.normpath(file_path)
        file.save(file_path_fix)
        filenames.append(filename) 

    return render_template('index.html', filenames=filenames, form_submitted=True, translate_pages=False)

@app.route('/translateWebtoon', methods=['POST'])
def translate_pages():
    uploaded_files = request.files.getlist('files[]')

    if not os.path.exists('Website/app/static/translatedPages'):
        os.makedirs('Website/app/static/translatedPages')

    # Call controller to translate pages saved uploaded by user.
    controller.TranslateWebtoons()

    translated_pages_dir = "Website/app/static/translatedPages"

    # Since this is mockup, there is no translation process this will just reupload the saved pages.
    filenames = []
    for filename in os.listdir(translated_pages_dir):
        filenames.append(filename)

    return render_template('index.html', filenames=filenames, form_submitted=False, translate_pages=True)