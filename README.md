
# GoogleDriveAccess
Access to google spreadsheet content.

### Dependent module:  
(Maybe needs sudo)

1. Google APIs Client Library => pip install --upgrade google-api-python-client  
	(The version of google-api-python-client above 1.4.0 will install fail in Mac OSX. <br> 
Please downgrade install => pip install -I google-api-python-client==1.3.2 <br>
reference:<http://stackoverflow.com/questions/29190604/attribute-error-trying-to-run-gmail-api-quickstart-in-python>)
2. Httplib2 => pip install httplib2

### Execute steps:

1. Change [client_secret], [client_email] and [client_id] to proper value in "client_secrets.json" file that get from Google Console <br>
	(Reference:<https://github.com/jay0lee/GAM/wiki/Creating-client_secrets.json-and-oauth2service.json>)
2. python googleDriveAccess.py
3. Copy Google Sheet File_ID and paste to console.
4. Copy Access Token from browser and paste to console.
5. Got exported file.

### Settings:

1. Open googleDriveAccess.py
2. Modify  
	FILE_NAME: file name for save  
	SAVE_PATH: the path for save file  
	FILE_ID: Google spreadsheet file_id got from page address  

### NOTIFICATION:

1. If got AttributeError: 'Module_six_moves_urllib_parse' in Mac OS. Execute following command  
	=> easy_install --upgrade six  
  It cause by the module version of "six" doesn't synchronized in different Python package.  

	We can check the version by following steps:  
>  	a. pip show six  
>  	b. $ pytho  
>		\>> import six; six.\__version__  
