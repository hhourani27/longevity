from pathlib import Path
import shutil
import mwclient

DIR = 'C:/Users/HabibElHourani/Desktop/tools/test2/longevity/data/assets'
SITE = mwclient.Site('commons.wikimedia.org')
EXTENSIONS = ['tiff','tif']
REPLACE = False

#%% Get files in category

categories = [
    'TIFF files of books',
    'TIFF files of books in Italian',
    'Biographie d’Alfred de Musset, sa vie et ses œuvres (2001)',
    'Revue de métaphysique et de morale'
    ]


for category_name in categories : 
    print()
    print('=======================')
    print('Searching category: ' + category_name)
    print('=======================')
    print()

    category = SITE.Categories[category_name]
    category_path = Path(DIR).joinpath(category_name)
    
    # If REPLACE = TRUE, delete and recreate category folder
    if REPLACE :
        if category_path.exists():
            shutil.rmtree(category_path)
        category_path.mkdir()
    # Else, create it if it doesn't already exist
    else :
        if not category_path.exists():
            category_path.mkdir()
    
    
    files = category.members(namespace=6)
    
    i = 0
    for file in files:
        i = i+1
        
        file_name = file.page_title
        print('Downloading file {:d}: {} ({:d} Mb)'.format(i,file_name,int(file.imageinfo['size']/1000000)))
        
        # If we specify an extension, ignore files that does not have this extension
        if EXTENSIONS :
            if not file_name.lower().endswith(tuple(EXTENSIONS)) :
                print('>> Ignored : wrong extension')
                continue
        
        file_path = category_path.joinpath(file_name.replace('"', ''))

        # If we don't replace, ignore files that are already there
        if not REPLACE : 
            if file_path.exists():
                print('>> Ignored : file already downloaded')
                continue
        
        file_path.write_bytes(file.download())
        

