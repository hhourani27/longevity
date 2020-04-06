from pathlib import Path
import shutil
import mwclient

DIR = 'C:/Users/HabibElHourani/Desktop/tools/test2/longevity/data/assets'

site = mwclient.Site('commons.wikimedia.org')

categories = [
    'Audio files of music of Germany',
    'Music magazines of Germany'
    ]

for category_name in categories : 
    category = site.Categories[category_name]
    category_path = Path(DIR).joinpath(category_name)
    if category_path.exists():
        shutil.rmtree(category_path)
        
    category_path.mkdir()
    
    files = category.members(namespace=6)
    for file in files:
        file_name = file.page_title
        file_path = category_path.joinpath(file_name)
        file_path.write_bytes(file.download())
