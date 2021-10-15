from flask import Blueprint, render_template, request, redirect, url_for
from src.website.static import sender

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        subject = request.form.get('object')
        content = request.form.get('content')
        emails = request.form.get('emails')
        sender.mail_sending(subject, content, emails)
        return redirect(url_for('index.success'))
    return render_template('index.html')


@index.route('/success')
def success():
    return render_template('success.html')
