from flask import Blueprint, render_template, request

index = Blueprint('index', __name__)


@index.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        object = request.form.get('object')
        content = request.form.get('content')
        emails = request.form.get('emails')

    return render_template('index.html')


@index.route('/success')
def success():
    return render_template('success.html')
