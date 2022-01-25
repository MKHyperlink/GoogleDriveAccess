#!/usr/bin/python

"""Google Drive Quickstart in Python.

This script uploads a single file to Google Drive.
"""

import pprint

import httplib2
import apiclient.discovery
import apiclient.http
import oauth2client.client
from oauth2client import tools
from oauth2client.file import Storage
import webbrowser
import os

import fileOperate

#Export file name
FILE_NAME = "language.csv"	
#Export file path
SAVE_PATH = "./%s" %(FILE_NAME)
#Google spreadsheet file_id
FILE_ID = ""

#spreadsheet tab id
GID_FIRST_PAGE = "0" #first tab
gid = GID_FIRST_PAGE

if not FILE_ID:
	FILE_ID = input('Enter Google spreadsheet File ID: ').strip()

if not gid:
	gid = input('Enter Google spreadsheet GID for specific tab if needed: ').strip()

# OAuth 2.0 scope that will be authorized.
# Check https://developers.google.com/drive/scopes for all available scopes.
OAUTH2_SCOPE = 'https://www.googleapis.com/auth/drive'

# Location of the client secrets.
CLIENT_SECRETS = 'client_secrets.json'

# Path to the file to upload.
FILENAME = 'document.txt'

# Metadata about the file.
MIMETYPE = 'text/plain'
TITLE = 'My New Text Document'
DESCRIPTION = 'A shiny new text document about hello world.'

APPLICATION_NAME = 'Google Drive Access'

def get_credentials():
    """Gets valid user credentials from storage.

    If nothing has been stored, or if the stored credentials are invalid,
    the OAuth2 flow is completed to obtain the new credentials.

    Returns:
        Credentials, the obtained credential.
    """

    try:
        import argparse
        flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
    except ImportError:
        flags = None

    home_dir = os.path.expanduser('~')
    credential_dir = os.path.join(home_dir, '.credentials')
    if not os.path.exists(credential_dir):
        os.makedirs(credential_dir)
    credential_path = os.path.join(credential_dir, 'googleDriveAccess.json')

    store = Storage(credential_path)
    credentials = store.get()
    if not credentials or credentials.invalid:
        flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRETS, OAUTH2_SCOPE)
        flow.user_agent = APPLICATION_NAME
        if flags:
            credentials = tools.run_flow(flow, store, flags)
        else: # Needed only for compatibility with Python 2.6
            credentials = tools.run(flow, store)
        print('Storing credentials to ' + credential_path)
    return credentials

def get_credentials_by_input():
	# Perform OAuth2.0 authorization flow.
	flow = oauth2client.client.flow_from_clientsecrets(CLIENT_SECRETS, OAUTH2_SCOPE)
	flow.redirect_uri = oauth2client.client.OOB_CALLBACK_URN
	authorize_url = flow.step1_get_authorize_url()
	# print 'Go to the following link in your browser: ' + authorize_url
	webbrowser.open_new_tab(authorize_url)
	code = input('Enter verification code: ').strip()
	return flow.step2_exchange(code)

credentials = get_credentials()

# Create an authorized Drive API client.
http = httplib2.Http()
credentials.authorize(http)
drive_service = apiclient.discovery.build('drive', 'v2', http=http)

file = fileOperate.get_file(drive_service, FILE_ID)
content = fileOperate.download_file(drive_service, file, gid)
fileOperate.save_file(content, SAVE_PATH);

# Insert a file. Files are comprised of contents and metadata.
def uploadFile():
	# MediaFileUpload abstracts uploading file contents from a file on disk.
	media_body = apiclient.http.MediaFileUpload(
	    FILENAME,
	    mimetype=MIMETYPE,
	    resumable=True
	)
	# The body contains the metadata for the file.
	body = {
	  'title': TITLE,
	  'description': DESCRIPTION,
	}
	# Perform the request and print the result.
	new_file = drive_service.files().insert(body=body, media_body=media_body).execute()
	pprint.pprint(new_file)


