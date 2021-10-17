import os
from src.website.static import sender
from src.website.static import txt_parser
from src.website.static import excel_parser
from flask import (Blueprint, render_template,
                   request, redirect, url_for)

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        subject = request.form.get('object')
        content = request.form.get('content')
        emails = request.form.get('emails')

        file = request.files['file']
        if file:
            cwd = os.getcwd() + r"\website\static\uploads"
            file_path = os.path.join(cwd, file.filename)
            file.save(file_path)
            if file.filename.rsplit('.', 1)[1].lower() == 'txt':
                filetype = 'text'
            else:
                filetype = 'excel'
            print(txt_parser.text(file_path))
            emails = txt_parser.text(file_path)
            print(emails)
        sender.mail_sending(subject, content, emails.strip())
        return redirect(url_for('index.success'))
    return render_template('index.html')


@index.route('/success')
def success():
    return render_template('success.html')
