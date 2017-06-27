###############################################################################
#                           MONGO INTERFACE FUNCTIONS                         #
###############################################################################



import pymongo
from datetime import date

# Load MongoDB client configuration
dbClient = pymongo.MongoClient("localhost", 27017)
db = dbClient.webimages


def get_domains(NSFW=True):
    """
    Loads the available domain names to be crawled within the database.
    The NSFW option indicates if sites with adult content should be included.
    Returns a list of domain names and the associated page to start with.
    """
    domains = list(db.SFW_domains.find())
    if NSFW :
        domains += list(db.NSFW_domains.find())
    return domains


# schema :
# {
#   url                     : String
#   indexed                 : Boolean (default = False)
#   dct_hash                : unsingned Int 64 bit
#   origin_domains          : [
#       String+
#   ]
# ////////// TO DO //////////////
#   last-validation-date    : Date
#   fileValid               : Boolean
#   file-dimensions        : {
#       size    : Int
#       height  : Int
#       width   : Int
#   }
# }


def insert_image(image_obj):
    """
    Inserts an image url into the BDD.
    If the url already exists : add the domain name to the image collection
    If the domain already exists : skips the addition
    Returns the image object inserted
    """

    image_res = db.images.find_one({"url" : image_obj["image_url"]})
    if image_res :
        image_res["webpages_urls"] = list(set( image_res["webpages_urls"] + [image_obj["webpage_url"]] ))
    else :
        image_res = {
            "url" : image_obj["image_url"],
            "webpages_urls" : [image_obj["webpage_url"]],
            "indexed" : False,
            "dct_hash" : int(0)
        }

    db.images.update( {"url":image_res["url"]}, image_res, upsert=True )
    
    return image_res