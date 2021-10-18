import os
from src.website.static import sender
from src.website.static import txt_parser
from werkzeug.utils import secure_filename
from src.website.static import excel_parser
from flask import (Blueprint, render_template,
                   request, redirect, url_for)

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        subject = request.form.get('object')
        content = request.form.get('content')
        email = request.form.get('emails').strip()
        emails = email.split("\n")
        file = request.files['file']
        if file:
            cwd = os.getcwd() + r"\website\static\uploads"
            filename = secure_filename(file.filename)
            file_path = os.path.join(cwd, filename)
            file.save(file_path)
            if file.filename.rsplit('.', 1)[1].lower() == 'txt':
                emails = txt_parser.text(file_path)
            else:
                emails = excel_parser.excel(file_path)
            os.remove(file_path)
        sender.mail_sending(subject, content, emails)

        return redirect(url_for('index.success'))
    return render_template('index.html')


@index.route('/success')
def success():
    return render_template('success.html')
