from pathlib import Path
import shutil
import mwclient

DIR = 'C:/Users/HabibElHourani/Desktop/tools/test2/longevity/data/images'

site = mwclient.Site('commons.wikimedia.org')

categories = [
    'Apocalypse flamande - BNF Néerl3'
    ]

for category_name in categories : 
    category = site.Categories[category_name]
    category_path = Path(DIR).joinpath(category_name)
    if category_path.exists():
        shutil.rmtree(category_path)
        
    category_path.mkdir()
    
    images = category.members(namespace=6)
    for img in images:
        file_name = img.page_title
        file_path = category_path.joinpath(file_name)
        file_path.write_bytes(img.download())
