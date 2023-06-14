from app import app
from flask import render_template, request, redirect, url_for, flash

@app.route('/', methods=['GET', 'POST'])
def home():
    return render_template('home.html')