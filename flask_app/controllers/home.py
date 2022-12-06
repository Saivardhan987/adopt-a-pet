from flask import Flask, render_template, request, redirect, session

from flask_app import app


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/login')
def login():
    if 'user_id' in session:
        return redirect('/search')
    return render_template('login.html')


@app.route("/logout")
def logout():
    session.clear()
    return redirect('/')
