from flask import Flask, render_template, request, redirect, session, flash

from flask_app import app
from flask_app.models.user import User
from flask_app.models.pet import Pet

from werkzeug.utils import secure_filename
import os


@app.route('/search')
def search_pet():
    if 'user_id' not in session:
        return redirect('/login')

    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)

    if 'pets' not in globals():
        pets = Pet.get_all()

    return render_template('search.html', user=user, pets=pets)


@app.route('/search/filtrar', methods=['POST'])
def search_filter():
    if 'user_id' not in session:
        return redirect('/login')

    data = {
        'location': request.form['location'],
        'type': request.form['type']
    }

    user = User.get_by_id({'id': session['user_id']})

    pets = Pet.get_filtered(data)
    return render_template('search.html', user=user, pets=pets)


@app.route('/search/add')
def add_pet():
    if 'user_id' not in session:
        return redirect('/login')

    return render_template('new_pet.html', user_id=session['user_id'])


@app.route('/search/create', methods=['POST'])
def create_pet():
    if 'user_id' not in session:
        return redirect('/login')

    if Pet.validate(request.form) == False:
        return redirect('/search/add')

    # Validaciones de la imagen
    if 'image' not in request.files:
        flash('Image not found', 'pets')
        return redirect('/search/add')

    image = request.files['image']

    if image.filename == '':
        flash('Empty image name', 'pets')
        return redirect('/search/add')

    image_name = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))

    form_data = {
        'name': request.form['name'],
        'description': request.form['description'],
        'type': request.form['type'],
        'age': request.form['age'],
        'location': request.form['location'],
        'phone': request.form['phone'],
        'gender': request.form['gender'],
        'user_id': request.form['user_id'],
        'image': image_name
    }

    Pet.save(form_data)
    return redirect('/search')


@app.route('/destroy/<id>')
def destroy(id):
    if 'user_id' not in session:
        return redirect('/login')

    Pet.destroy({'id': id})
    return redirect('/posts')


@app.route('/edit/<id>')
def edit(id):
    if 'user_id' not in session:
        return redirect('login')
    pet = Pet.get_by_id({'id': id})

    return render_template('edit_pet.html', pet=pet, user_id=session['user_id'])


@app.route('/update', methods=['POST'])
def update_pet():
    if 'user_id' not in session:
        return redirect('/login')

    if Pet.validate(request.form) == False:
        return redirect('/search/add')

    # Image Validation
    if 'image' not in request.files:
        flash('Image not found', 'pets')
        return redirect('/search/add')

    image = request.files['image']

    if image.filename == '':
        flash('Empty image name', 'pets')
        return redirect('/search/add')

    image_name = secure_filename(image.filename)
    image.save(os.path.join(app.config['UPLOAD_FOLDER'], image_name))

    form_data = {
        'id': request.form['id'],
        'name': request.form['name'],
        'description': request.form['description'],
        'type': request.form['type'],
        'age': request.form['age'],
        'location': request.form['location'],
        'phone': request.form['phone'],
        'gender': request.form['gender'],
        'user_id': request.form['user_id'],
        'image': image_name
    }

    Pet.update(form_data)
    return redirect('/search')


@app.route('/posts')
def manage_posts():
    if 'user_id' not in session:
        return redirect('/login')
    data = {
        'id': session['user_id']
    }
    user = User.get_by_id(data)
    pets = Pet.get_all_by_user_id({'user_id': session['user_id']})
    return render_template('manage_posts.html', user=user, pets=pets)


@app.route('/show')
def show_pet():
    return render_template('show_pet.html')
