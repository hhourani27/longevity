from flask import render_template, flash, redirect, url_for, request, make_response
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
from app import app, db
from app.forms.forms import LoginForm, AssetUploadForm, AssetGetForm, CollectionGetForm
from app.models.user import User,Organisation
from app.models.asset import DigitalAsset, Collection
from app.models.storage import AssetStorageHistory, DataStorageLocation
from app.models.format import Format
from app.services.asset import AssetService, CollectionService
from app.services.storage import StorageService
from app.services.format import FormatService

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


@app.route('/')
@app.route('/dashboard')
@login_required
def dashboard():
    total_asset_count = AssetService.count()
    total_collection_count = CollectionService.count()
    total_read_count = StorageService.getDataReadCount()
        
    collections = CollectionService.get_all()
    collection_asset_count = [AssetService.count(c) for c in collections]
    collection_read_count = [StorageService.getDataReadCount(c) for c in collections]

    storage_locations = StorageService.getStorageLocations(used_only = True)
    storage_regions = StorageService.getStorageRegions(used_only = True)
    storage_providers = StorageService.getDataProviders(used_only = True)
    
    return render_template('dashboard.html', title='Home', 
        total_asset_count=total_asset_count, 
        total_collection_count=total_collection_count, 
        total_read_count = total_read_count,
        collections = collections,
        collection_asset_count = collection_asset_count,
        collection_read_count = collection_read_count,
        storage_locations=storage_locations,
        storage_regions = storage_regions,
        storage_providers = storage_providers
        )

@app.route('/collection', defaults={'id': None}, methods=['GET'])
@app.route('/collection/<id>', methods=['GET'])
@login_required
def collection(id) :
    collections = CollectionService.get_all()
    collections_to_select = [(col.id,col.name) for col in collections]
    
    collection_select_form = CollectionGetForm(collections_to_select)
    
    if id is not None :
        # Get collection
        collection = Collection.query.filter_by(id=id, organisation_id=current_user.organisation_id).first()
        
        # If no collection of this id exists in this organisation
        if collection is None :
            return render_template('collection.html', title='Collection', collection_select_form=collection_select_form, collection=collection, searched_id=id)
            
        # Get collection statistics
        asset_count = AssetService.count(collection)
        
        storage_locations = StorageService.getStorageLocations(collection=collection, used_only = True)
        storage_regions = StorageService.getStorageRegions(collection=collection, used_only = True)
        storage_providers = StorageService.getDataProviders(collection=collection, used_only = True)
        
        read_count = StorageService.getDataReadCount(collection)
        
        # Recreate collection select form with default value
        collection_select_form = CollectionGetForm(collections_to_select, default=id)
    
        return render_template('collection.html', title='Collection',
                collection = collection,
                collection_select_form=collection_select_form,
                asset_count = asset_count,
                read_count = read_count,
                storage_locations = storage_locations,
                storage_regions = storage_regions,
                storage_providers = storage_providers
                )
    
    else :
        return render_template('collection.html', title='Collection', collection_select_form=collection_select_form)
    
    

@app.route('/asset', defaults={'id': None}, methods=['GET'])
@app.route('/asset/<id>', methods=['GET'])
@login_required
def asset_info(id):
    form = AssetGetForm()
    if id is not None :
        # Get asset
        asset = DigitalAsset.query.filter_by(id=id, organisation_id=current_user.organisation_id).first()
        
        # If no asset of this id exists in this organisation
        if asset is None :
            return render_template('asset.html', title='Asset', form=form, asset=asset, searched_id=id)
        
        # Get storage location
        storage_locations = [asl.data_storage_location for asl in asset.storage_locations]
        
        # Get asset history
        asset_history = asset.asset_history.all()        
        storage_history = asset.storage_history.all()
        history_list = asset_history + storage_history
        history_list.sort(key = lambda h: h.timestamp, reverse=True)
        
        history_table = []
        for h in history_list:
            detail = h.storage_location.data_provider.name + " : " + h.storage_location.name if isinstance(h,AssetStorageHistory) else ''
            history_table.append((h.timestamp, h.event, detail))
        
        # Pre-fill search bar
        form.id.data = id
        
        return render_template('asset.html', title='Asset', form=form, asset=asset, storage_locations=storage_locations, history_table=history_table, searched_id=id)
    else:
        return render_template('asset.html', title='Asset', form=form)


@app.route('/asset/<id>/data', methods=['GET'])
@login_required
def asset_data(id):
    asset = AssetService.get(id)
    mime_type = '{}/{}'.format(asset.format.media,asset.format.name)
    data = StorageService.getAssetData(asset)
    
    response = make_response(data)
    response.headers.set('Content-Type', mime_type)
    response.headers.set('Content-Disposition', 'attachment', filename=asset.filename)
    return response


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = AssetUploadForm()
    
    # Populate combo boxes
    form.collection.choices = [(col.id,col.name) for col in CollectionService.get_all()]
    form.format.choices = [(f.id,f.display_name()) for f in FormatService.get_all()]
    
    if form.validate_on_submit():
        filename = secure_filename(form.file.data.filename)
        digital_asset = DigitalAsset(name=form.name.data, format_id=form.format.data, filename=filename, organisation_id=current_user.organisation_id, collection_id=form.collection.data)

        # Get file data and save it to byte array
        data = form.file.data.read()
        form.file.data.close()
        
        # Create and store data
        AssetService.add_and_store(digital_asset,data)
        
        return redirect(url_for('asset_info') + '/' + str(digital_asset.id))

    
    return render_template('upload.html', title='Upload asset', form=form)

@app.route('/doc/storage/<id>', methods=['GET'])
@login_required
def doc_storage(id):
    storage_location = DataStorageLocation.query.get(id)
    
    return render_template('doc_storage.html', title='Storage', storage_location=storage_location)

@app.route('/doc/format', methods=['GET'])
@login_required
def doc_format():
    return render_template('doc_format.html', title='Format')
    
@app.route('/doc/continuite', methods=['GET'])
@login_required
def doc_continuite():
    return render_template('doc_continuite.html', title='Continuité')