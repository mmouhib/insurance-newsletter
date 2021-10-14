from flask import Blueprint, render_template

index = Blueprint('index', __name__)

@index.route('/')
def home():
    return render_template('index.html')

@index.route('/success')
def success():
    return render_template('success.html')