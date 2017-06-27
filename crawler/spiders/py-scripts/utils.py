###############################################################################
#                               UTILITY FUNCTIONS                             #
###############################################################################


def load_config(file_path):
    '''
    Loads a configuration file given a file_path.
    Returns the config object extracted.
    Will raise an Exception if the file can't be loaded.
    '''
    config_file = open(file_path)
    config = loads(config_file.read(), encoding="utf8")
    return config



def valid_ext (url):
    '''
    Checks if the image format is valid regarding the specifications of 
    the project. Returns true if valid, else false.
    '''
    ext = url.split(".")[-1].lower()

    # Add any new valid extension here.
    if ext in ["jpg", "jpeg", "png"]:
        return True
    
    return False