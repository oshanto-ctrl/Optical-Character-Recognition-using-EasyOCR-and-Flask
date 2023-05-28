#importing necessary libraries
from flask import * # bad practice (import only necessaries)
from werkzeug.utils import secure_filename
import os
import easyocr
import urllib.request

# Flask app instance
app = Flask(__name__)


UPLOAD_FOLDER = "static/images/"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['SECRET_KEY'] = "my-secret-key"
app.config['DEBUG'] = True
app.config['MAX_CONTENT_PATH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['jpg', 'jpeg', 'png'])
languageFormData = {}

# Index page
@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == "POST":
        lang1 = request.form['l1']
        lang2 = request.form['l2']

        languageFormData['l1'] = lang1
        languageFormData['l2'] = lang2
        # return redirect(url_for('upload_image'))
        return render_template('upload_image.html')
    else:
        return render_template('index.html', title='Project OCR')

pic = {}

# Function for uploading images
@app.route('/upload_image', methods=['POST', 'GET'])
def upload_image():
    if request.method == "POST":
        f = request.files['file']
        filename = secure_filename(f.filename)
        f.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # f.save(secure_filename(f.filename))

        print(filename)
        pic['x'] = f 
        print("PIC UPLOADED.")

        
        l1 = languageFormData['l1']
        l2 = languageFormData['l2']
        
        # img = pic['x']
        print("l1 = ", l1 , " l2 = ", l2 , " pic = ", f)
        reader = easyocr.Reader([l1, l2], gpu=False)
        # results = reader.readtext(f)
        
        results = reader.readtext(filename)
        text = ""
        for r in results:
            text += r[1]
        print(text)


        return render_template('index.html', l1=languageFormData['l1'], l2=languageFormData['l2'], result=text)
    else:
        print("UPLOAD FAILED.")
        # return render_template('upload_image.html')
        return redirect(request.url)

"""
@app.route('/success', methods=['POST', 'GET'])
def success():
    l1 = languageFormData['l1']
    l2 = languageFormData['l2']
    img = pic['x']
    print("l1 = ", l1 , " l2 = ", l2 , " pic = ", img)
    reader = easyocr.Reader([l1, l2], gpu=False)
    results = reader.readtext(img)
    text = ""
    for r in results:
        text += r[1]
    print(text)

    return render_template('success.html', l1=languageFormData['l1'], l2=languageFormData['l2'], result=text, title="success page")
"""


if __name__ == '__main__':
    app.run(debug=True) # Discard debug=True at production.



