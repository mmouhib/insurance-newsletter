from flask import Blueprint, render_template, request, redirect, url_for
from src.website.static import sender
from src.website.static import txt_parser
import os

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        subject = request.form.get('object')
        content = request.form.get('content')
        emails = request.form.get('emails')

        if request.files:
            file = request.files['file']
            cwd = os.getcwd() + r"/website/static/uploads"
            file.save(os.path.join(cwd, file.filename))

        #     if file.filename.rsplit('.', 1)[1].lower() == 'txt':
        #         filetype = 'text'
        #     else:
        #         filetype = 'excel'
        #
        # if filetype == 'text':
        emails = txt_parser.text(cwd+'/'+file.filename)

        sender.mail_sending(subject, content, emails)
        return redirect(url_for('index.success'))
    return render_template('index.html')


@index.route('/success')
def success():
    return render_template('success.html')
