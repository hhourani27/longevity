import os
from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app import app, db
from app.forms import LoginForm, AssetUploadForm
from app.models import User,Organisation
from app.asset_models import DigitalAsset


@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    user = {'username': 'Miguel'}
    return render_template('dashboard.html', title='Home', user=user)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('dashboard')
        return redirect(next_page)

    return render_template('login.html', title='Sign In', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = AssetUploadForm()
    if form.validate_on_submit():
        asset = DigitalAsset(name=form.name.data,type=form.type.data,organisation_id=current_user.organisation.id)

        f = form.file.data
        filename = secure_filename(f.filename)
        f.save(os.path.join(
            app.config['STORAGE_FILE_LOCATION'], filename
        ))
        
        db.session.add(asset)
        db.session.commit()
        
        return redirect(url_for('upload'))

    return render_template('upload.html', form=form)
