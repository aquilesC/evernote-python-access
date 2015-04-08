""" EVERNOTE LOGIN
    ~~~~~~~~~~~~~~
    Python script that allows to log in into Evernote by opening a simple Qt browser window. 
    Before launching the program, check that you have edited the config.example file with your
    default parameters. 
"""
    
# Evernote Imports
from evernote.api.client import EvernoteClient

# Import the OAuth class (it is a PyQt Main window)
from evernote_oauth import get_token
# Config import
from config import CONSUMER_SECRET, CONSUMER_KEY, DEV_MODE, NOTE_URL

def parse_query_string(authorize_url):
    """ Simple function for extracting the OAuth parameters from an URL
    """
    uargs = authorize_url.split('?')
    vals = {}
    if len(uargs) == 1:
        raise Exception('Invalid Authorization URL')
    for pair in uargs[1].split('&'):
        key, value = pair.split('=', 1)
        vals[key] = value
    return vals

if DEV_MODE:
    sdb = True
else:
    sdb = False
    
# Create the Evernote Client
client = EvernoteClient(
    consumer_key = CONSUMER_KEY,
    consumer_secret = CONSUMER_SECRET,
    sandbox = sdb)


request_token = client.get_request_token(NOTE_URL)
authorize_url = client.get_authorize_url(request_token)

token_url = get_token(authorize_url)
vals = parse_query_string(token_url)

access_token = client.get_access_token(
    request_token['oauth_token'],
    request_token['oauth_token_secret'],
    vals['oauth_verifier'])

client = EvernoteClient(token=access_token)
client = EvernoteClient(token=access_token)
userStore = client.get_user_store()
user = userStore.getUser()
limit = user.accounting.uploadLimit
print('The username is: %s'%(user.username))
print('The current limit is %s MB'%(limit/1024/1024))
