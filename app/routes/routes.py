from flask import render_template, flash, redirect, url_for
from flask import request
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app import app, db
from app.forms.forms import LoginForm, AssetUploadForm, AssetGetForm
from app.models.user import User,Organisation
from app.models.asset import DigitalAsset
from app.services.asset import AssetManager
from app.services.storage import StorageManager


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

@app.route('/asset', defaults={'id': None}, methods=['GET'])
@app.route('/asset/<id>', methods=['GET'])
@login_required
def asset_info(id):
    form = AssetGetForm()
    if id is not None :
        asset = DigitalAsset.query.filter_by(id=id, organisation_id=current_user.organisation_id).first()
        return render_template('asset.html', title='Asset', form=form, asset=asset)
    else:
        return render_template('asset.html', title='Asset', form=form)

@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = AssetUploadForm()
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        digital_asset = DigitalAsset(name=form.name.data, type=form.type.data, filename=filename, organisation_id=current_user.organisation.id)        
        AssetManager.add_and_store(digital_asset,form.file.data)
        
        print("ICI")
        print(digital_asset.id)
        return redirect(url_for('asset_info') + '/' + str(digital_asset.id))

    return render_template('upload.html', title='Upload asset', form=form)
    