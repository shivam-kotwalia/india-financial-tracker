from flask import render_template
from . import app

@app.route('/')
def home():
    return render_template('base.html')

@app.route('/about')
def about():
    return render_template('about.html')  # Assuming an about.html template will be created later.