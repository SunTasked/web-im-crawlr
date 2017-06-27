import os
import wget
import requests

def create_dir(new_dir):
    """
    Checks if the specified direcory does exists
    Creates it if that is not the case
    """
    os.makedirs(new_dir,exist_ok=True)

def download_image(url, destination):
    wget.download(url=url, out=destination)
    """filename = destination + url.split('/')[-1]
    with open(filename, 'wb') as handle:
            response = requests.get(url, stream=True)
            if not response.ok:
                pass
            for block in response.iter_content(1024):
                if not block:
                    break
                handle.write(block)"""


import pymongo
from datetime import date

# Load MongoDB client configuration
dbClient = pymongo.MongoClient("localhost", 27017)
db = dbClient.webimages
images = list(db.images.find())

create_dir("./downloaded")
failed_dl = 0

failed_file = open("./failed_dls.txt", mode='w')
urls_file = open("./urls.txt", mode='w')

for idx, image in enumerate(images):
    print(str(idx) + "/" + str(len(images)) + " : " + image["url"])
    urls_file.write(image["url"] + "\n")

    try :
        download_image(image["url"], "./downloaded/")
    except :
        print()
        print("download failed -- skipping to next picture")
        failed_file.write(image["url"] + "\n")
        failed_dl+=1
    print()

print("failed dls : " + str(failed_dl))
print()

urls_file.close()
failed_file.close()