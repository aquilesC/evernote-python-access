""" Example Configuration File.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~
    
    Change the parameters you need to change 
    (specially CONSUMER_KEY and CONSUMER_SECRET) and save the file as config.py
    
    These parameters will be read in the main program to log in into Evernote. 
    
    Ideally we can redirect the user to a local page asking the user to close the window.
"""
    

USER_BASE_URL = "www.evernote.com" # This is where the user will be redirected after log in.
USER_STORE_URI = "https://www.evernote.com/edam/user"
CONSUMER_KEY = "..."
CONSUMER_SECRET = "..."

USER_BASE_URL_SANDBOX = "sandbox.evernote.com"  # This is where the user will be redirected after log in.
USER_STORE_URI_SANDBOX = "https://sandbox.evernote.com/edam/user"
CONSUMER_KEY_SANDBOX = "..."
CONSUMER_SECRET_SANDBOX = "..."

# Evernote config
VERSION = 0.1

DEV_MODE = 1

if DEV_MODE:
    USER_STORE_URI = USER_STORE_URI_SANDBOX
    CONSUMER_KEY = CONSUMER_KEY_SANDBOX
    CONSUMER_SECRET = CONSUMER_SECRET_SANDBOX
    USER_BASE_URL = USER_BASE_URL_SANDBOX

# Url view the note
NOTE_URL = "https://%domain%/Home.action?#n=%s"

NOTE_URL = NOTE_URL.replace('%domain%', USER_BASE_URL)